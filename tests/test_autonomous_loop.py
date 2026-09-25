from app.core.autonomous_loop import AutonomousLoop

def test_autonomous_cycle():
    loop = AutonomousLoop()
    res = loop.execute_autonomous_cycle("Optimize database queries")
    assert res["status"] == "success"
    assert res["iteration"] == 1
    assert res["goal"] == "Optimize database queries"
    assert res["next_state"] == "monitoring"
