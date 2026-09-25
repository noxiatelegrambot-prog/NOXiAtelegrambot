from app.core.user_profiling import UserProfilingEngine

def test_user_profiling_analytics():
    engine = UserProfilingEngine()
    user_id = 42
    
    engine.record_interaction(user_id, "dialogue")
    engine.record_interaction(user_id, "dialogue")
    engine.record_interaction(user_id, "telemetry_check")

    profile = engine.get_user_profile(user_id)
    assert profile["total_interactions"] == 3
    assert profile["favorite_action"] == "dialogue"
    assert profile["actions"]["dialogue"] == 2
