from app.core.faz1_final_integration import Faz1FinalIntegration

def test_faz1_smoke_test():
    result = Faz1FinalIntegration.run_smoke_test()
    assert result["status"] == "success"
    assert len(result["completed_steps"]) == 6
    assert "successfully verified" in result["message"]
