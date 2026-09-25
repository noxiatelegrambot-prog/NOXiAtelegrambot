from app.core.conversational_memory import ConversationalMemoryManager

def test_conversational_memory_flow():
    manager = ConversationalMemoryManager()
    user = "user_123"
    
    assert manager.add_turn(user, "user", "Selam!") is True
    assert manager.add_turn(user, "assistant", "Aleykümselam, nasılsın?") is True
    
    history = manager.get_history(user)
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[1]["content"] == "Aleykümselam, nasılsın?"

    assert manager.clear_history(user) is True
    assert len(manager.get_history(user)) == 0
