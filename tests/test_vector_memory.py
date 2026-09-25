
from app.core.vector_memory import VectorMemoryEngine

def test_vector_memory_semantic_search():
    engine = VectorMemoryEngine()
    engine.add_vector_memory("doc1", "Python 3.13 asynchronous Telegram bot development", {"category": "dev"})
    engine.add_vector_memory("doc2", "Ankara public transport neighborhood boundaries", {"category": "geo"})
    engine.add_vector_memory("doc3", "Python backend asynchronous architecture", {"category": "dev"})

    results = engine.semantic_search("Python asynchronous bot", top_k=2)
    assert len(results) > 0
    assert results[0]["id"] == "doc1"
