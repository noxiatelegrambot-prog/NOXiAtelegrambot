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

def test_search_experiences_roundtrip(tmp_path):
    async def run():
        from app.memory.database import initialize_memory, save_experience, search_experiences
        db_file = tmp_path / "test_noxia.db"
        db_path = str(db_file)
        
        await initialize_memory(db_file)
        
        await save_experience(
            db_path,
            task_id="task_001",
            situation="Web research failed due to timeout",
            action="Tried alternative search query",
            result="Success",
            lesson="Use fallback source when first source fails",
            success=True
        )
        
        await save_experience(
            db_path,
            task_id="task_002",
            situation="Database connection error",
            action="Reconnected to SQLite",
            result="Success",
            lesson="Ensure connection close handling",
            success=True
        )
        
        results = await search_experiences(db_path, "web research timeout")
        assert len(results) > 0
        assert "Web research failed" in results[0]["situation"]
        
        empty_results = await search_experiences(db_path, "nonexistentquery12345")
        assert len(empty_results) == 0

    import asyncio
    asyncio.run(run())

def test_orchestrator_experience_integration(tmp_path):
    async def run():
        from app.memory.database import initialize_memory, save_experience, search_experiences
        db_file = tmp_path / "test_noxia.db"
        db_path = str(db_file)
        
        await initialize_memory(db_file)
        await save_experience(
            db_path,
            task_id="task_prev",
            situation="Api timeout on provider",
            action="Switch to fallback provider",
            result="Success",
            lesson="Always use fallback when primary fails",
            success=True
        )
        
        task_query = "Api timeout error"
        experiences = await search_experiences(db_path, task_query)
        
        assert len(experiences) > 0
        assert "fallback" in experiences[0]["lesson"]

    import asyncio
    asyncio.run(run())


def test_memory_category_filtering(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        await save_memory(database, "category_a", "First item")
        await save_memory(database, "category_b", "Second item")

        results = await search_memories(database, "item")
        assert len(results) == 2

    asyncio.run(run())


def test_multiple_agent_runs_and_failures(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        from app.memory.database import save_agent_run, get_agent_runs

        # Success run
        await save_agent_run(
            database,
            task_id="task_multi",
            agent="developer",
            input_text="Write code",
            output_text="Code written successfully",
            success=True,
            duration_ms=500
        )

        # Failure run
        await save_agent_run(
            database,
            task_id="task_multi",
            agent="tester",
            input_text="Run tests",
            output_text="AssertionError: 1 failed",
            success=False,
            duration_ms=300
        )

        runs = await get_agent_runs(database, task_id="task_multi")
        assert len(runs) == 2
        
        # Verify success and failure records
        success_runs = [r for r in runs if r["success"] is True]
        failure_runs = [r for r in runs if r["success"] is False]
        
        assert len(success_runs) == 1
        assert success_runs[0]["agent"] == "developer"
        
        assert len(failure_runs) == 1
        assert failure_runs[0]["agent"] == "tester"
        assert "AssertionError" in failure_runs[0]["output_text"]

    asyncio.run(run())
