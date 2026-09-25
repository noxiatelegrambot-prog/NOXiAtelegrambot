from app.core.master_orchestrator import MasterOrchestrationCore

def test_master_orchestration_core():
    orchestrator = MasterOrchestrationCore()
    
    result = orchestrator.process_global_pipeline(101, "Sistem durum raporu ver")
    assert result["status"] == "executed_successfully"
    assert "NOXiA Master Core processed" in result["response"]
    assert result["telemetry_ref"]["active_subsystems_count"] == 5
    assert len(orchestrator.orchestration_log) == 1
