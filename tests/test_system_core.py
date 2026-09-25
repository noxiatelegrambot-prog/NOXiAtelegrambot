from app.core.system_core import SystemCore

def test_system_initialization():
    init = SystemCore.initialize_system()
    assert init["status"] == "operational"
    assert init["ready"] is True
    assert len(init["components"]) == 4

def test_safe_execute_success():
    def sample(x):
        return x * 2
    res = SystemCore.safe_execute(sample, 5)
    assert res["status"] == "success"
    assert res["result"] == 10

def test_safe_execute_error():
    def faulty():
        raise ValueError("Simulated failure")
    res = SystemCore.safe_execute(faulty)
    assert res["status"] == "error"
    assert "Simulated failure" in res["message"]
