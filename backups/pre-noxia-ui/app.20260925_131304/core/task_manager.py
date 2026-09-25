import uuid

class TaskLifecycleManager:
    VALID_STATES = {"pending", "planned", "running", "completed", "failed", "cancelled"}

    @staticmethod
    def create_task(title: str) -> dict:
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        return {
            "task_id": task_id,
            "title": title,
            "state": "pending"
        }

    @staticmethod
    def transition_state(current_state: str, new_state: str) -> str:
        if new_state in TaskLifecycleManager.VALID_STATES:
            return new_state
        return current_state
