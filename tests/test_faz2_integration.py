from app.core.faz2_integration import Faz2Integration

def test_faz2_full_system_smoke_test():
    res = Faz2Integration.run_faz2_smoke_test()
    assert res["status"] == "success"
    assert res["faz_2_completed"] is True
    assert res["total_autonomous_subsystems"] == 9
    assert "SandboxManager" in res["subsystems"]
    assert "AutonomousLoop" in res["subsystems"]
    assert "TelemetryManager" in res["subsystems"]
