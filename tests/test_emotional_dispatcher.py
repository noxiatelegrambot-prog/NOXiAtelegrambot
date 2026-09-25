from app.core.emotional_dispatcher import EmotionalDispatcher

def test_emotional_dispatcher_routing():
    dispatcher = EmotionalDispatcher()
    
    # Test urgent routing
    result_urgent = dispatcher.process_message(123, "Acil durum: sistem çöküyor!")
    assert result_urgent["tone"] == "urgent"
    assert result_urgent["action"] == "initiate_emergency_health_check"

    # Test standard routing
    result_std = dispatcher.process_message(123, "Merhaba NOXiA")
    assert result_std["tone"] == "neutral"
    assert result_std["action"] == "standard_dialogue_response"
