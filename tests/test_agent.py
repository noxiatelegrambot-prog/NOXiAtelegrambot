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


def test_multi_agent_workflow(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        from app.agent.core import ResearcherAgent, SummarizerAgent
        from app.memory.database import get_agent_runs

        task_id = "task-workflow-001"

        researcher = ResearcherAgent(name="researcher", database_path=database)
        summarizer = SummarizerAgent(name="summarizer", database_path=database)

        # Step 1: Researcher agent gathers info
        research_result = await researcher.execute(task_id, "NOXiA autonomous architecture")
        assert "Researched topic" in research_result

        # Step 2: Summarizer agent processes researcher's output
        summary_result = await summarizer.execute(task_id, research_result)
        assert "Summarized: Researched topic" in summary_result

        # Verify audit trails in database
        runs = await get_agent_runs(database, task_id=task_id)
        assert len(runs) == 2
        assert runs[0]["agent"] == "researcher"
        assert runs[1]["agent"] == "summarizer"

    asyncio.run(run())


import pytest


def test_faulty_agent_error_handling(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        from app.agent.core import FaultyTestAgent
        from app.memory.database import get_agent_runs

        task_id = "task-fault-001"
        agent = FaultyTestAgent(name="faulty_agent", database_path=database)

        # Execution should raise ValueError on "fail" input
        with pytest.raises(ValueError, match="Intentional failure for testing"):
            await agent.execute(task_id, "Please fail this task")

        # Verify failure is recorded in database with success=False
        runs = await get_agent_runs(database, task_id=task_id)
        assert len(runs) == 1
        assert runs[0]["agent"] == "faulty_agent"
        assert runs[0]["success"] is False
        assert "Intentional failure for testing" in runs[0]["output_text"]

    asyncio.run(run())
