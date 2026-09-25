import time

class AutonomousTaskScheduler:
    def __init__(self):
        self.scheduled_tasks = {}
        self.execution_log = []

    def register_task(self, task_name: str, interval_seconds: int, callback):
        self.scheduled_tasks[task_name] = {
            "interval": interval_seconds,
            "callback": callback,
            "last_executed": 0
        }

    def tick(self, current_time: float) -> list:
        executed_now = []
        for name, task in self.scheduled_tasks.items():
            if current_time - task["last_executed"] >= task["interval"]:
                try:
                    task["callback"]()
                    task["last_executed"] = current_time
                    executed_now.append(name)
                    self.execution_log.append({"task": name, "time": current_time, "status": "success"})
                except Exception as e:
                    self.execution_log.append({"task": name, "time": current_time, "status": "error", "reason": str(e)})
        return executed_now
