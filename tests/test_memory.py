import asyncio

from app.memory.database import (
    initialize_memory,
    save_memory,
    search_memories,
)


def test_memory_roundtrip(tmp_path):
    async def run():
        database = tmp_path / "test.db"

        await initialize_memory(database)

        await save_memory(
            database,
            "experience",
            "NOXiA memory test",
        )

        results = await search_memories(
            database,
            "NOXiA memory test",
        )

        assert len(results) == 1
        assert results[0][1] == "experience"
        assert results[0][2] == "NOXiA memory test"

    asyncio.run(run())


def test_agent_run_roundtrip(tmp_path):
    async def run():
        database = tmp_path / "test.db"

        await initialize_memory(database)

        from app.memory.database import save_agent_run, get_agent_runs

        await save_agent_run(
            database,
            task_id="task-001",
            agent="researcher",
            input_text="Test query",
            output_text="Test result",
            success=True,
            duration_ms=1250,
        )

        results = await get_agent_runs(
            database,
            task_id="task-001",
        )

        assert len(results) == 1
        assert results[0]["agent"] == "researcher"
        assert results[0]["success"] is True
        assert results[0]["duration_ms"] == 1250

    asyncio.run(run())


def test_experience_roundtrip(tmp_path):
    async def run():
        database = tmp_path / "test.db"

        await initialize_memory(database)

        from app.memory.database import (
            save_experience,
            get_experiences,
        )

        await save_experience(
            database,
            task_id="task-002",
            situation="Web research failed",
            action="Tried alternative source",
            result="Research succeeded",
            lesson="Use a fallback source when the first source fails",
            success=True,
        )

        results = await get_experiences(
            database,
            task_id="task-002",
        )

        assert len(results) == 1
        assert results[0]["task_id"] == "task-002"
        assert results[0]["situation"] == "Web research failed"
        assert results[0]["action"] == "Tried alternative source"
        assert results[0]["result"] == "Research succeeded"
        assert results[0]["lesson"] == (
            "Use a fallback source when the first source fails"
        )
        assert results[0]["success"] is True

    asyncio.run(run())
