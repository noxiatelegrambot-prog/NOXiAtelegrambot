from dataclasses import dataclass
from typing import Any


@dataclass
class AgentResult:
    agent: str
    success: bool
    output: str
    data: dict[str, Any] | None = None


class BaseAgent:
    name = "base"

    async def run(self, task) -> AgentResult:
        raise NotImplementedError
