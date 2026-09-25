
import uuid
import time

class TaskLifecycle:
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class CentralController:
    def __init__(self):
        self.tasks = {}

    def create_task(self, title: str, task_type: str = "general") -> dict:
        task_id = str(uuid.uuid4())[:8]
        task = {
            "id": task_id,
            "title": title,
            "type": task_type,
            "status": TaskLifecycle.PENDING,
            "progress": 0,
            "created_at": time.time()
        }
        self.tasks[task_id] = task
        return task

    def update_task_status(self, task_id: str, status: str, progress: int = None):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = status
            if progress is not None:
                self.tasks[task_id]["progress"] = progress
            return True
        return False

    def get_task(self, task_id: str) -> dict:
        return self.tasks.get(task_id)
