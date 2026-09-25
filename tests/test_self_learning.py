from app.core.self_learning_agent import SelfLearningAgent

def test_learning_feedback():
    success_res = SelfLearningAgent.process_learning_feedback({"status": "success"})
    assert success_res["learning_status"] == "recorded"
    assert success_res["memory_updated"] is True

    fail_res = SelfLearningAgent.process_learning_feedback({"status": "failed"})
    assert fail_res["learning_status"] == "analyzed_failure"
    assert "Failure mode logged" in fail_res["insight"]
