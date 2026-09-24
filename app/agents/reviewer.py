from app.agents.base import AgentResult, BaseAgent


class Reviewer(BaseAgent):
    name = "reviewer"

    async def run(self, task) -> AgentResult:
        return AgentResult(
            agent=self.name,
            success=True,
            output=(
                "Değişiklik inceleme aşaması tamamlandı. "
                "Production'a doğrudan değişiklik uygulanmadı."
            ),
            data={
                "task_id": task.id,
                "production_write": False,
            },
        )
