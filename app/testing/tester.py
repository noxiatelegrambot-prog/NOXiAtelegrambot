from app.agents.base import AgentResult, BaseAgent


class Tester(BaseAgent):
    name = "tester"

    async def run(self, task) -> AgentResult:
        return AgentResult(
            agent=self.name,
            success=True,
            output=(
                "Test aşaması hazır. "
                "Compile, unit, integration ve regression testleri bağlanacak."
            ),
            data={"task": task.prompt},
        )
