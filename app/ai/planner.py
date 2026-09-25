
import json

class PlannerError(Exception):
    pass

class TaskPlanner:
    def __init__(self):
        self.supported_agent_types = ["research", "developer", "tester", "reviewer"]

    def analyze_and_plan(self, prompt: str) -> dict:
        if not prompt or not isinstance(prompt, str):
            raise PlannerError("Invalid prompt provided for planning.")

        prompt_lower = prompt.lower()
        agents = []

        # Determine required agents based on keywords
        if "araştır" in prompt_lower or "search" in prompt_lower or "bul" in prompt_lower:
            agents.append("research")
        if "kod" in prompt_lower or "yaz" in prompt_lower or "patch" in prompt_lower or "oluştur" in prompt_lower:
            agents.append("developer")
        if "test" in prompt_lower or "kontrol" in prompt_lower:
            agents.append("tester")
        
        # Default fallback if no specific agent matched
        if not agents:
            agents = ["research", "developer"]

        # Always include reviewer for quality assurance if code or dev is involved
        if "developer" in agents and "reviewer" not in agents:
            agents.append("reviewer")

        plan = {
            "task_summary": prompt[:50],
            "agents": agents,
            "requires_review": "reviewer" in agents,
            "status": "valid"
        }
        return plan

    def validate_plan(self, plan: dict) -> bool:
        if not isinstance(plan, dict):
            return False
        if "agents" not in plan or not isinstance(plan["agents"], list):
            return False
        return len(plan["agents"]) > 0
