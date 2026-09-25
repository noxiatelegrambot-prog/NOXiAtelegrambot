from app.core.task_manager import TaskLifecycleManager

def test_task_creation():
    task = TaskLifecycleManager.create_task("Test Task")
    assert task["state"] == "pending"
    assert "task_id" in task

def test_state_transitions():
    state = TaskLifecycleManager.transition_state("pending", "running")
    assert state == "running"

    invalid_state = TaskLifecycleManager.transition_state("running", "unknown_state")
    assert invalid_state == "running"
