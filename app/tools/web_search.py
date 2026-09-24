import os
from openai import AsyncOpenAI


async def web_search(query: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is required for real web research."
        )

    client = AsyncOpenAI(api_key=api_key)

    response = await client.responses.create(
        model=os.getenv("NOXIA_RESEARCH_MODEL", "gpt-5"),
        tools=[{"type": "web_search_preview"}],
        input=query,
    )

    return {
        "query": query,
        "output": response.output_text,
    }
