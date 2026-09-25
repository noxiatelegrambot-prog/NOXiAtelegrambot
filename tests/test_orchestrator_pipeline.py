from app.core.orchestrator_pipeline import OrchestratorPipeline

def test_orchestrator_stages():
    res = OrchestratorPipeline.execute_pipeline_step("plan", {"task": "Build feature"})
    assert res["status"] == "success"
    assert res["stage"] == "plan"

    error_res = OrchestratorPipeline.execute_pipeline_step("invalid_stage", {})
    assert error_res["status"] == "error"
