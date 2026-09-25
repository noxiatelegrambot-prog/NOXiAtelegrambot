from app.core.relationship_memory import RelationshipMemoryEngine

def test_relationship_memory_storage():
    engine = RelationshipMemoryEngine()
    user = "user_999"

    assert engine.store_fact(user, "favorite_topic", "Python Telegram Bots") is True
    assert engine.store_fact(user, "coding_style", "Clean and modular") is True

    topic = engine.recall_fact(user, "favorite_topic")
    assert topic == "Python Telegram Bots"

    summary = engine.get_user_profile_summary(user)
    assert summary["stored_facts_count"] == 2
    assert summary["facts"]["coding_style"] == "Clean and modular"

def test_recall_nonexistent_fact():
    engine = RelationshipMemoryEngine()
    assert engine.recall_fact("unknown_user", "anything") is None
