import os
from dataclasses import dataclass

import httpx


@dataclass
class AIResult:
    provider: str
    model: str
    text: str


class AIProvider:
    name = "base"

    async def generate(self, prompt: str) -> AIResult:
        raise NotImplementedError


class GeminiProvider(AIProvider):
    name = "gemini"

    async def generate(self, prompt: str) -> AIResult:
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY is not configured")

        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                url,
                params={"key": key},
                json={
                    "contents": [
                        {"parts": [{"text": prompt}]}
                    ]
                },
            )
            response.raise_for_status()
            data = response.json()

        text = data["candidates"][0]["content"]["parts"][0]["text"]

        return AIResult(self.name, model, text)


class AnthropicProvider(AIProvider):
    name = "anthropic"

    async def generate(self, prompt: str) -> AIResult:
        key = os.getenv("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is not configured")

        model = os.getenv(
            "ANTHROPIC_MODEL",
            "claude-sonnet-4-20250514",
        )

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json={
                    "model": model,
                    "max_tokens": 2048,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                },
            )
            response.raise_for_status()
            data = response.json()

        text = "".join(
            item.get("text", "")
            for item in data.get("content", [])
            if item.get("type") == "text"
        )

        return AIResult(self.name, model, text)


class OpenAIProvider(AIProvider):
    name = "openai"

    async def generate(self, prompt: str) -> AIResult:
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("OPENAI_API_KEY is not configured")

        model = os.getenv("OPENAI_MODEL", "gpt-5.4")

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
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
            response.raise_for_status()
            data = response.json()

        text = data.get("output_text", "")

        if not text:
            for item in data.get("output", []):
                for content in item.get("content", []):
                    if content.get("type") == "output_text":
                        text += content.get("text", "")

        return AIResult(self.name, model, text)


class AIRouter:
    def __init__(self):
        self.providers = {
            "gemini": GeminiProvider(),
            "anthropic": AnthropicProvider(),
            "openai": OpenAIProvider(),
        }

    def configured(self):
        order = os.getenv(
            "NOXIA_AI_ORDER",
            "gemini,anthropic,openai",
        )

        return [
            name.strip()
            for name in order.split(",")
            if name.strip() in self.providers
        ]

    async def generate(self, prompt: str) -> AIResult:
        errors = []

        for name in self.configured():
            try:
                return await self.providers[name].generate(prompt)
            except Exception as exc:
                errors.append(
                    f"{name}: {type(exc).__name__}: {exc}"
                )

        raise RuntimeError(
            "All AI providers failed.\n" + "\n".join(errors)
        )

    def status(self):
        keys = {
            "openai": os.getenv("OPENAI_API_KEY"),
            "gemini": os.getenv("GEMINI_API_KEY"),
            "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        }

        return {
            name: {
                "configured": bool(keys[name]),
                "model": (
                    os.getenv("OPENAI_MODEL", "gpt-5.4")
                    if name == "openai"
                    else os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
                    if name == "gemini"
                    else os.getenv(
                        "ANTHROPIC_MODEL",
                        "claude-sonnet-4-20250514",
                    )
                ),
            }
            for name in self.providers
        }
