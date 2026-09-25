from app.core.autonomous_loop import AutonomousLoopOrchestrator

def test_autonomous_loop_execution():
    orchestrator = AutonomousLoopOrchestrator()
    result = orchestrator.run_cycle("HTTP 409 Conflict during polling")

    assert result["status"] == "success"
    assert result["final_state"] == "committed"
    assert len(result["log"]) == 5
    assert "Analyzed error" in result["log"][0]
    assert "Committed changes" in result["log"][4]
