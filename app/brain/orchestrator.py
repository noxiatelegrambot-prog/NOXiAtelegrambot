import logging
from pathlib import Path

from app.agents.reviewer import Reviewer
from app.brain.planner import Planner
from app.coding.developer import Developer
from app.memory.database import log_task, save_memory
from app.models.task import Task, TaskStatus
from app.research.researcher import Researcher
from app.testing.tester import Tester

logger = logging.getLogger("noxia.brain")


class Orchestrator:
    def __init__(self, database_path: Path | None = None):
        self.database_path = database_path
        self.planner = Planner()

        self.researcher = Researcher()
        self.developer = Developer()
        self.tester = Tester()
        self.reviewer = Reviewer()

        self.active_tasks: dict[str, Task] = {}

    async def create_task(self, prompt, source="telegram"):
        task = Task(prompt=prompt, source=source)
        task.plan = self.planner.create_plan(prompt)

        self.active_tasks[task.id] = task

        if self.database_path:
            await log_task(self.database_path, task)

        return task

    async def execute(self, task):
        task.status = TaskStatus.RUNNING

        results = []

        if self.database_path:
            await log_task(self.database_path, task)

        try:
            for step in task.plan:
                if step == "research":
                    result = await self.researcher.run(task)
                elif step == "develop":
                    result = await self.developer.run(task)
                elif step == "test":
                    result = await self.tester.run(task)
                elif step == "verify":
                    result = await self.reviewer.run(task)
                else:
                    continue

                results.append(result)

                if not result.success:
                    raise RuntimeError(
                        f"{result.agent} failed: {result.output}"
                    )

            task.result = "\n\n".join(
                f"[{r.agent}] {r.output}" for r in results
            )

            task.status = TaskStatus.COMPLETED

            if self.database_path:
                await log_task(self.database_path, task)
                await save_memory(
                    self.database_path,
                    "experience",
                    f"{task.prompt} => {' -> '.join(task.plan)}",
                )

        except Exception as exc:
            task.status = TaskStatus.FAILED
            task.error = str(exc)

            if self.database_path:
                await log_task(self.database_path, task)

            logger.exception("Task failed | id=%s", task.id)

        return task

    async def run(self, prompt, source="telegram"):
        task = await self.create_task(prompt, source)
        return await self.execute(task)
