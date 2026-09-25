from app.core.empathy_engine import EmpathyEngine

def test_empathy_mood_tracking():
    engine = EmpathyEngine()
    user = "user_456"
    
    strategy1 = engine.update_mood(user, "neutral")
    assert strategy1 == "balanced_and_attentive"

    strategy2 = engine.update_mood(user, "positive")
    assert strategy2 == "enthusiastic_and_engaging"

def test_supportive_strategy_on_frustration():
    engine = EmpathyEngine()
    user = "user_789"
    
    engine.update_mood(user, "frustrated")
    strategy = engine.update_mood(user, "frustrated")
    assert strategy == "supportive_and_calming"
