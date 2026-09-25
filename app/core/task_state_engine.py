class TaskStateEngine:
    VALID_TRANSITIONS = {
        "pending": ["planned", "cancelled"],
        "planned": ["running", "cancelled"],
        "running": ["completed", "failed", "cancelled"],
        "failed": ["pending", "cancelled"],
        "completed": [],
        "cancelled": []
    }

    @staticmethod
    def validate_transition(current_state: str, target_state: str) -> bool:
        allowed = TaskStateEngine.VALID_TRANSITIONS.get(current_state, [])
        return target_state in allowed

    @staticmethod
    def create_task(task_id: str, title: str) -> dict:
        return {
            "task_id": task_id,
            "title": title,
            "state": "pending",
            "history": [{"state": "pending", "note": "Task created"}]
        }

    @staticmethod
    def transition_task(task: dict, target_state: str) -> dict:
        current_state = task["state"]
        if TaskStateEngine.validate_transition(current_state, target_state):
            task["state"] = target_state
            task["history"].append({"state": target_state, "note": f"Transitioned from {current_state}"})
            return {"status": "success", "task": task}
        return {"status": "error", "message": f"Invalid transition from {current_state} to {target_state}"}
