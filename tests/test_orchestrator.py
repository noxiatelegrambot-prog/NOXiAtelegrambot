from app.core.orchestrator import Orchestrator

def test_orchestrator_pipeline():
    orch = Orchestrator()
    res = orch.execute_pipeline("Build authentication feature")
    assert res["status"] == "success"
    assert res["pipeline_stages_count"] == 6
    assert len(res["execution_trace"]) == 6
    assert res["execution_trace"][0]["stage"] == "analyze"
    assert res["execution_trace"][-1]["stage"] == "verify"

def test_orchestrator_dependency_graph():
    orch = Orchestrator()
    assert orch.validate_dependency_graph() is True
