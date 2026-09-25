class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    async def execute(self, task_context: dict) -> dict:
        raise NotImplementedError("Ajanexecute metodunu ezmelidir.")
