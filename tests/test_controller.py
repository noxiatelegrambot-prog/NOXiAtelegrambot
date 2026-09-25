
from app.core.controller import CentralController, TaskLifecycle

def test_central_controller_task_lifecycle():
    controller = CentralController()
    task = controller.create_task("Analyze Repository", task_type="dev")
    
    task_id = task["id"]
    assert task["status"] == TaskLifecycle.PENDING
    assert task["progress"] == 0

    # Update to running
    controller.update_task_status(task_id, TaskLifecycle.RUNNING, progress=50)
    updated = controller.get_task(task_id)
    assert updated["status"] == TaskLifecycle.RUNNING
    assert updated["progress"] == 50

    # Update to completed
    controller.update_task_status(task_id, TaskLifecycle.COMPLETED, progress=100)
    completed = controller.get_task(task_id)
    assert completed["status"] == TaskLifecycle.COMPLETED
    assert completed["progress"] == 100
