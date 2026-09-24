import asyncio
from pathlib import Path
from app.memory.database import initialize_memory, get_agent_runs
from app.agent.core import SimpleOrchestratorAgent


def test_simple_orchestrator_agent(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        agent = SimpleOrchestratorAgent(name="orchestrator", database_path=database)
        result = await agent.execute(task_id="task-agent-001", input_text="Hello autonomous world")

        assert "Processed: Hello autonomous world" in result

        runs = await get_agent_runs(database, task_id="task-agent-001")
        assert len(runs) == 1
        assert runs[0]["agent"] == "orchestrator"
        assert runs[0]["success"] is True

    asyncio.run(run())
