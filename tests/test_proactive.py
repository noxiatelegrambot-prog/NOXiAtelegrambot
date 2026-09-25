from app.core.proactive_engagement import ProactiveEngagementEngine

def test_proactive_hook_with_interests():
    res = ProactiveEngagementEngine.generate_proactive_prompt(["Telegram bot development", "Python"])
    assert res["status"] == "success"
    assert res["interest_targeted"] == "Telegram bot development"
    assert "Telegram bot development" in res["hook"]

def test_proactive_hook_default():
    res = ProactiveEngagementEngine.generate_proactive_prompt([])
    assert res["status"] == "default"
    assert "hangi projeler" in res["hook"]
