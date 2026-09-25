
class LearningEngine:
    def __init__(self):
        self.lessons_learned = []

    def evaluate_execution(self, task_result: dict) -> dict:
        status = task_result.get("status", "unknown")
        if status == "success":
            lesson = {"type": "success_pattern", "detail": "Task completed successfully without errors."}
        else:
            lesson = {"type": "failure_pattern", "detail": f"Task failed: {task_result.get('error', 'unknown error')}"}
        
        self.lessons_learned.append(lesson)
        return lesson

    def get_insights(self) -> list:
        return self.lessons_learned
