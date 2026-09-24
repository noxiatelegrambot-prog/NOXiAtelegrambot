from app.agents.base import AgentResult, BaseAgent


class Researcher(BaseAgent):
    name = "researcher"

    async def run(self, task) -> AgentResult:
        return AgentResult(
            agent=self.name,
            success=True,
            output=(
                "Araştırma aşaması hazır. "
                "Kaynak toplama motoru bu aşamaya bağlanacak."
            ),
            data={"query": task.prompt},
        )
