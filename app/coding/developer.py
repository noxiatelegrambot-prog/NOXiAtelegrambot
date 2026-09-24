from app.agents.base import AgentResult, BaseAgent


class Developer(BaseAgent):
    name = "developer"

    async def run(self, task) -> AgentResult:
        return AgentResult(
            agent=self.name,
            success=True,
            output=(
                "Geliştirme aşaması hazır. "
                "Kod analizi ve kontrollü patch sistemi bu aşamaya bağlanacak."
            ),
            data={"task": task.prompt},
        )
