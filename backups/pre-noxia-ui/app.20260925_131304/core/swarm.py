
class Blackboard:
    def __init__(self):
        self.data = {}
        self.messages = []

    def post(self, key: str, value: any):
        self.data[key] = value

    def read(self, key: str) -> any:
        return self.data.get(key)

    def broadcast(self, sender: str, message: str):
        self.messages.append({"sender": sender, "message": message})

    def get_feed(self) -> list:
        return self.messages

class SwarmCoordinator:
    def __init__(self):
        self.blackboard = Blackboard()
        self.agents = []

    def register_agent(self, agent_name: str):
        self.agents.append(agent_name)

    def coordinate_task(self, task_description: str) -> dict:
        self.blackboard.post("current_task", task_description)
        self.blackboard.broadcast("Coordinator", f"Started task: {task_description}")
        return {
            "status": "coordinated",
            "registered_agents": len(self.agents),
            "blackboard_data": self.blackboard.data
        }
