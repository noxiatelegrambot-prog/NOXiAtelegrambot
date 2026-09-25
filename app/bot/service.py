from pathlib import Path
from app.agent.core import SimpleOrchestratorAgent, ResearcherAgent, SummarizerAgent
from app.memory.database import save_memory, get_memories


class BotService:
    def __init__(self, database_path: Path):
        self.database_path = database_path
        self.orchestrator = SimpleOrchestratorAgent(name="bot_orchestrator", database_path=database_path)
        self.researcher = BotService._init_agent(ResearcherAgent, "bot_researcher", database_path)
        self.summarizer = BotService._init_agent(SummarizerAgent, "bot_summarizer", database_path)

    @staticmethod
    def _init_agent(agent_cls, name, db_path):
        return agent_cls(name=name, database_path=db_path)

    async def handle_message(self, task_id: str, user_message: str) -> str:
        # Save user interaction memory with category
        await save_memory(self.database_path, task_id=task_id, category="interaction", content=f"User: {user_message}")

        # Route through orchestrator or specialized agent based on command/content
        if "research" in user_message.lower():
            result = await self.researcher.execute(task_id, user_message)
        elif "summarize" in user_message.lower():
            result = await self.summarizer.execute(task_id, user_message)
        else:
            result = await self.orchestrator.execute(task_id, user_message)

        # Save assistant response memory with category
        await save_memory(self.database_path, task_id=task_id, category="interaction", content=f"Assistant: {result}")
        return result
