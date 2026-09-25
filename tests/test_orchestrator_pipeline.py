from app.core.orchestrator_pipeline import OrchestratorPipeline

def test_pipeline_execution():
    OrchestratorPipeline.init_pipeline_db()
    res = OrchestratorPipeline.execute_task_pipeline("task_999", "Refactor Telegram UI Dispatcher")
    
    assert res["status"] == "SUCCESS"
    assert len(res["steps"]) == 3
    assert "Developer Agent" in res["steps"][0]
    assert "Sandbox" in res["steps"][1]
    assert "Tester Agent" in res["steps"][2]
