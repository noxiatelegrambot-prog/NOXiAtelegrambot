import pytest
import asyncio
from app.brain.orchestrator import Orchestrator
from app.memory.database import initialize_memory, save_experience

def test_orchestrator_retrieves_experience(tmp_path):
    async def run():
        db_file = tmp_path / "test_noxia.db"
        
        await initialize_memory(db_file)
        await save_experience(
            str(db_file),
            task_id="task_old",
            situation="Network timeout during web research",
            action="Retry with fallback URL",
            result="Success",
            lesson="Always provide fallback options for network calls",
            success=True
        )
        
        orchestrator = Orchestrator(db_path=str(db_file))
        experiences = await orchestrator.get_relevant_experiences("Network timeout web research")
        
        assert len(experiences) > 0
        assert "fallback" in experiences[0]["lesson"]

    asyncio.run(run())
