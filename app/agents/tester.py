from app.agents.base import AgentResult, BaseAgent
from app.tools.test_runner import run_tests


class Tester(BaseAgent):
    name = "tester"

    async def run(self, task) -> AgentResult:
        try:
            result = await run_tests()

            return AgentResult(
                agent=self.name,
                success=result["success"],
                output=result["output"],
                data={
                    "task_id": task.id,
                    "command": result["command"],
                    "returncode": result["returncode"],
                    "real_test_run": True,
                },
            )
        except Exception as exc:
            return AgentResult(
                agent=self.name,
                success=False,
                output=f"Tester error: {exc}",
                data={
                    "task_id": task.id,
                    "real_test_run": False,
                },
            )
