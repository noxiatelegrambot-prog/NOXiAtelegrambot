
import pytest
from app.core.memory import MemoryEngine

def test_memory_engine_add_and_search():
    engine = MemoryEngine()
    engine.add_memory("knowledge", "Python 3.13 is used for NOXiA backend.", importance=3)
    engine.add_memory("error", "HTTP 409 Conflict occurred during Telegram polling.", importance=2)

    # Case-insensitive search test
    results = engine.search_memories("telegram")
    assert len(results) == 1
    assert "Conflict" in results[0]["content"]

    # Category filter test
    knowledge_results = engine.search_memories("Python", category="knowledge")
    assert len(knowledge_results) == 1

    # Invalid category test
    with pytest.raises(ValueError):
        engine.add_memory("invalid_cat", "Should fail")
