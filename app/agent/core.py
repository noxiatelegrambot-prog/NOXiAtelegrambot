from pathlib import Path
from app.memory.database import save_agent_run


class BaseAgent:
    def __init__(self, name: str, database_path: Path):
        self.name = name
        self.database_path = database_path

    async def execute(self, task_id: str, input_text: str) -> str:
        raise NotImplementedError("Subclasses must implement execute method.")


class SimpleOrchestratorAgent(BaseAgent):
    async def execute(self, task_id: str, input_text: str) -> str:
        output_text = f"Processed: {input_text}"
        await save_agent_run(
            self.database_path,
            task_id=task_id,
            agent=self.name,
            input_text=input_text,
            output_text=output_text,
            success=True,
            duration_ms=100
        )
        return output_text


class ResearcherAgent(BaseAgent):
    async def execute(self, task_id: str, input_text: str) -> str:
        output_text = f"Researched topic: {input_text}"
        await save_agent_run(
            self.database_path,
            task_id=task_id,
            agent=self.name,
            input_text=input_text,
            output_text=output_text,
            success=True,
            duration_ms=150
        )
        return output_text


class SummarizerAgent(BaseAgent):
    async def execute(self, task_id: str, input_text: str) -> str:
        output_text = f"Summarized: {input_text}"
        await save_agent_run(
            self.database_path,
            task_id=task_id,
            agent=self.name,
            input_text=input_text,
            output_text=output_text,
            success=True,
            duration_ms=80
        )
        return output_text
