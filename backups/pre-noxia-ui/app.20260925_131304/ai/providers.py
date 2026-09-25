import asyncio
import os
import time
from dataclasses import dataclass

import httpx


@dataclass
class AIResult:
    provider: str
    model: str
    text: str


class AIProvider:
    name = "base"

    def configured(self) -> bool:
        return False

    async def generate(self, prompt: str) -> AIResult:
        raise NotImplementedError


class OpenRouterProvider(AIProvider):
    name = "openrouter"

    def configured(self):
        return bool(os.getenv("OPENROUTER_API_KEY"))

    async def generate(self, prompt):
        key = os.getenv("OPENROUTER_API_KEY")
        if not key:
            raise RuntimeError("OPENROUTER_API_KEY is not configured")

        model = os.getenv("OPENROUTER_MODEL", "openrouter/free")

        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                    "X-Title": "NOXiA",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            r.raise_for_status()
            data = r.json()

        text = data["choices"][0]["message"]["content"]

        if not text:
            raise RuntimeError("OpenRouter returned empty response")

        return AIResult(self.name, model, text)


class GroqProvider(AIProvider):
    name = "groq"

    def configured(self):
        return bool(os.getenv("GROQ_API_KEY"))

    async def generate(self, prompt):
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY is not configured")

        model = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile",
        )

        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            r.raise_for_status()
            data = r.json()

        text = data["choices"][0]["message"]["content"]

        if not text:
            raise RuntimeError("Groq returned empty response")

        return AIResult(self.name, model, text)


class GeminiProvider(AIProvider):
    name = "gemini"

    def configured(self):
        return bool(os.getenv("GEMINI_API_KEY"))

    async def generate(self, prompt):
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY is not configured")

        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

        url = (
            "https://generativelanguage.googleapis.com/"
            f"v1beta/models/{model}:generateContent"
        )

        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                url,
                params={"key": key},
                json={
                    "contents": [
                        {
                            "parts": [{"text": prompt}]
                        }
                    ]
                },
            )
            r.raise_for_status()
            data = r.json()

        text = data["candidates"][0]["content"]["parts"][0]["text"]

        return AIResult(self.name, model, text)


class HuggingFaceProvider(AIProvider):
    name = "huggingface"

    def configured(self):
        return bool(os.getenv("HF_TOKEN"))

    async def generate(self, prompt):
        key = os.getenv("HF_TOKEN")
        if not key:
            raise RuntimeError("HF_TOKEN is not configured")

        model = os.getenv(
            "HF_MODEL",
            "openai/gpt-oss-120b:groq",
        )

        async with httpx.AsyncClient(timeout=90) as client:
            r = await client.post(
                "https://router.huggingface.co/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            r.raise_for_status()
            data = r.json()

        text = data["choices"][0]["message"]["content"]

        if not text:
            raise RuntimeError("HuggingFace returned empty response")

        return AIResult(self.name, model, text)


class OpenAIProvider(AIProvider):
    name = "openai"

    def configured(self):
        return bool(os.getenv("OPENAI_API_KEY"))

    async def generate(self, prompt):
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("OPENAI_API_KEY is not configured")

        model = os.getenv("OPENAI_MODEL", "gpt-5.4")

        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                "https://api.openai.com/v1/responses",
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "input": prompt,
                },
            )
            r.raise_for_status()
            data = r.json()

        text = data.get("output_text", "")

        if not text:
            for item in data.get("output", []):
                for content in item.get("content", []):
                    if content.get("type") == "output_text":
                        text += content.get("text", "")

        if not text:
            raise RuntimeError("OpenAI returned empty response")

        return AIResult(self.name, model, text)


class AIRouter:
    def __init__(self):
        self.providers = {
            "openrouter": OpenRouterProvider(),
            "groq": GroqProvider(),
            "gemini": GeminiProvider(),
            "huggingface": HuggingFaceProvider(),
            "openai": OpenAIProvider(),
        }

        self.cooldowns = {}
        self.failures = {}

        self.cooldown_seconds = int(
            os.getenv("NOXIA_AI_COOLDOWN", "60")
        )

    def configured(self):
        default_order = (
            "openrouter,"
            "groq,"
            "gemini,"
            "huggingface,"
            "openai"
        )

        order = os.getenv(
            "NOXIA_AI_ORDER",
            default_order,
        )

        return [
            name.strip()
            for name in order.split(",")
            if name.strip() in self.providers
            and self.providers[name.strip()].configured()
        ]

    def _available(self, name):
        until = self.cooldowns.get(name, 0)
        return time.time() >= until

    def _mark_failure(self, name, exc):
        self.failures[name] = self.failures.get(name, 0) + 1

        message = str(exc).lower()

        quota_error = any(
            x in message
            for x in (
                "429",
                "quota",
                "rate limit",
                "rate_limit",
                "too many requests",
                "insufficient_quota",
                "resource exhausted",
            )
        )

        if quota_error:
            self.cooldowns[name] = (
                time.time() + self.cooldown_seconds
            )

    def _mark_success(self, name):
        self.failures[name] = 0
        self.cooldowns.pop(name, None)

    async def generate(self, prompt):
        errors = []

        for name in self.configured():
            if not self._available(name):
                remaining = int(
                    self.cooldowns[name] - time.time()
                )
                errors.append(
                    f"{name}: cooldown {max(remaining, 0)}s"
                )
                continue

            try:
                result = await self.providers[name].generate(prompt)

                if not result.text.strip():
                    raise RuntimeError("empty response")

                self._mark_success(name)
                return result

            except Exception as exc:
                self._mark_failure(name, exc)

                errors.append(
                    f"{name}: "
                    f"{type(exc).__name__}: {exc}"
                )

                await asyncio.sleep(0)

        if not self.configured():
            raise RuntimeError(
                "No AI providers configured."
            )

        raise RuntimeError(
            "All available AI providers failed.\n"
            + "\n".join(errors)
        )

    def status(self):
        result = {}

        for name, provider in self.providers.items():
            cooldown = self.cooldowns.get(name, 0)
            remaining = max(
                0,
                int(cooldown - time.time()),
            )

            if name == "openrouter":
                model = os.getenv(
                    "OPENROUTER_MODEL",
                    "openrouter/free",
                )
            elif name == "groq":
                model = os.getenv(
                    "GROQ_MODEL",
                    "llama-3.3-70b-versatile",
                )
            elif name == "gemini":
                model = os.getenv(
                    "GEMINI_MODEL",
                    "gemini-2.5-flash",
                )
            elif name == "huggingface":
                model = os.getenv(
                    "HF_MODEL",
                    "openai/gpt-oss-120b:groq",
                )
            else:
                model = os.getenv(
                    "OPENAI_MODEL",
                    "gpt-5.4",
                )

            result[name] = {
                "configured": provider.configured(),
                "available": (
                    provider.configured()
                    and remaining == 0
                ),
                "model": model,
                "failures": self.failures.get(name, 0),
                "cooldown_seconds": remaining,
            }

        return result
