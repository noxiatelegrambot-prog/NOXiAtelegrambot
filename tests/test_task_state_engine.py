from app.core.task_state_engine import TaskStateEngine

def test_task_valid_transitions():
    assert TaskStateEngine.validate_transition("pending", "planned") is True
    assert TaskStateEngine.validate_transition("planned", "running") is True
    assert TaskStateEngine.validate_transition("running", "completed") is True

def test_task_invalid_transitions():
    assert TaskStateEngine.validate_transition("pending", "completed") is False
    assert TaskStateEngine.validate_transition("completed", "running") is False

def test_task_lifecycle_execution():
    task = TaskStateEngine.create_task("task_001", "Refactor codebase")
    assert task["state"] == "pending"

    # Test invalid transition from pending directly to completed
    res_err = TaskStateEngine.transition_task(task, "completed")
    assert res_err["status"] == "error"
    assert task["state"] == "pending"

    res1 = TaskStateEngine.transition_task(task, "planned")
    assert res1["status"] == "success"
    assert task["state"] == "planned"

    res2 = TaskStateEngine.transition_task(task, "running")
    assert res2["status"] == "success"
    assert task["state"] == "running"

    res_ok = TaskStateEngine.transition_task(task, "completed")
    assert res_ok["status"] == "success"
    assert task["state"] == "completed"
