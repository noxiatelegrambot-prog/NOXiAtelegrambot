
class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.status = "idle"
        self.metadata = {}

    def execute(self, task_data: dict) -> dict:
        raise NotImplementedError("Subclasses must implement execute method.")

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Researcher", role="information_gathering")

    def execute(self, task_data: dict) -> dict:
        self.status = "running"
        query = task_data.get("query", "")
        result = {"status": "success", "findings": f"Gathered data for: {query}"}
        self.status = "idle"
        return result

class DeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Developer", role="code_generation")

    def execute(self, task_data: dict) -> dict:
        self.status = "running"
        spec = task_data.get("spec", "")
        result = {"status": "success", "code": f"# Generated code for: {spec}"}
        self.status = "idle"
        return result
