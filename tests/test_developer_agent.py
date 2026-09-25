from app.core.developer_agent import DeveloperAgent

def test_developer_agent_patch():
    res = DeveloperAgent.analyze_and_patch("main.py", "Add logging feature")
    assert res["status"] == "success"
    assert res["diff_valid"] is True
    assert "patch" in res
