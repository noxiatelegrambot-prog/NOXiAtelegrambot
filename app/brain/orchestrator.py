import logging
from pathlib import Path

from app.agents.reviewer import Reviewer
from app.agents.researcher import Researcher as AgentResearcher
from app.agents.tester import Tester as AgentTester
from app.ai.providers import AIRouter
from app.brain.planner import Planner
from app.coding.developer import Developer
from app.memory.database import log_task, save_memory
from app.models.task import Task, TaskStatus
from app.research.researcher import Researcher as LegacyResearcher
from app.testing.tester import Tester as LegacyTester

logger = logging.getLogger("noxia.brain")


class Orchestrator:
    def __init__(
        self,
        database_path: Path | None = None,
    ):
        self.database_path = database_path

        self.planner = Planner()
        self.ai_router = AIRouter()

        # Yeni gerçek agent'lar
        self.agent_researcher = AgentResearcher()
        self.agent_tester = AgentTester()

        # Mevcut kontrollü developer/reviewer
        self.developer = Developer()
        self.reviewer = Reviewer()

        # Eski agent'lar fallback olarak korunuyor.
        self.legacy_researcher = LegacyResearcher()
        self.legacy_tester = LegacyTester()

        self.active_tasks: dict[str, Task] = {}

    async def create_task(
        self,
        prompt,
        source="telegram",
    ):
        task = Task(
            prompt=prompt,
            source=source,
        )

        task.plan = self.planner.create_plan(prompt)

        self.active_tasks[task.id] = task

        if self.database_path:
            await log_task(
                self.database_path,
                task,
            )

        return task

    async def execute(self, task):
        task.status = TaskStatus.RUNNING

        results = []

        if self.database_path:
            await log_task(
                self.database_path,
                task,
            )

        try:
            for step in task.plan:

                if step == "research":
                    result = await self.agent_researcher.run(task)

                elif step == "develop":
                    result = await self.developer.run(task)

                elif step == "test":
                    result = await self.agent_tester.run(task)

                elif step == "verify":
                    result = await self.reviewer.run(task)

                else:
                    continue

                results.append(result)

                if not result.success:
                    raise RuntimeError(
                        f"{result.agent} failed: "
                        f"{result.output}"
                    )

            task.result = "\n\n".join(
                f"[{r.agent}] {r.output}"
                for r in results
            )

            task.status = TaskStatus.COMPLETED

            if self.database_path:
                await log_task(
                    self.database_path,
                    task,
                )

                await save_memory(
                    self.database_path,
                    "experience",
                    (
                        f"{task.prompt} => "
                        f"{' -> '.join(task.plan)}"
                    ),
                )

        except Exception as exc:
            task.status = TaskStatus.FAILED
            task.error = str(exc)

            if self.database_path:
                await log_task(
                    self.database_path,
                    task,
                )

            logger.exception(
                "Task failed | id=%s",
                task.id,
            )

        finally:
            self.active_tasks.pop(
                task.id,
                None,
            )

        return task

    async def run(
        self,
        prompt,
        source="telegram",
    ):
        task = await self.create_task(
            prompt,
            source,
        )

        return await self.execute(task)

    async def ask_ai(self, prompt: str):
        """
        Genel AI isteği için provider fallback.
        Örn:
        Gemini başarısız -> Anthropic ->
        OpenAI.
        """
        return await self.ai_router.generate(prompt)

    def ai_status(self):
        return self.ai_router.status()
