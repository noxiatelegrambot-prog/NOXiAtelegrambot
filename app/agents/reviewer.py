from app.agents.base import AgentResult, BaseAgent


class Reviewer(BaseAgent):
    name = "reviewer"

    async def run(self, task) -> AgentResult:
        return AgentResult(
            agent=self.name,
            success=True,
            output=(
                "Review aşaması hazır. "
                "Değişikliklerin güvenlik ve kalite kontrolü burada yapılacak."
            ),
            data={"task": task.prompt},
        )
