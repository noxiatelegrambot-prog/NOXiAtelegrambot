import asyncio
from pathlib import Path
from app.memory.database import initialize_memory, get_memories, get_agent_runs
from app.bot.service import BotService


def test_bot_service_routing(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        service = BotService(database_path=database)
        task_id = "task-bot-001"

        # Test standard routing (orchestrator)
        res1 = await service.handle_message(task_id, "Hello NOXiA")
        assert "Processed: Hello NOXiA" in res1

        # Test research routing
        res2 = await service.handle_message(task_id, "Please research quantum computing")
        assert "Researched topic" in res2

        # Test summarize routing
        res3 = await service.handle_message(task_id, "Please summarize the findings")
        assert "Summarized" in res3

        # Verify memories were stored
        memories = await get_memories(database, task_id=task_id)
        assert len(memories) >= 6  # User + Assistant pairs

        # Verify agent runs were logged
        runs = await get_agent_runs(database, task_id=task_id)
        assert len(runs) == 3

    asyncio.run(run())
