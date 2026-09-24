from app.agents.base import AgentResult, BaseAgent
from app.tools.web_search import web_search


class Researcher(BaseAgent):
    name = "researcher"

    async def run(self, task) -> AgentResult:
        query = getattr(task, "description", None) or getattr(task, "prompt", None) or str(task)

        try:
            result = await web_search(query)

            return AgentResult(
                agent=self.name,
                success=True,
                output=result["output"],
                data={
                    "task_id": task.id,
                    "query": result["query"],
                    "real_web_search": True,
                    "result_count": len(result["results"]),
                },
            )
        except Exception as exc:
            return AgentResult(
                agent=self.name,
                success=False,
                output=f"Researcher error: {exc}",
                data={
                    "task_id": task.id,
                    "real_web_search": False,
                },
            )
