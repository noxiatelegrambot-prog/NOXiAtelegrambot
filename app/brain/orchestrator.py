import logging

from app.models.task import Task, TaskStatus

logger = logging.getLogger("noxia.brain")


class Orchestrator:
    def __init__(self):
        self.active_tasks: dict[str, Task] = {}

    async def create_task(self, prompt: str, source: str = "telegram") -> Task:
        task = Task(prompt=prompt, source=source)
        self.active_tasks[task.id] = task

        logger.info(
            "Task created | id=%s | source=%s | prompt=%s",
            task.id,
            task.source,
            task.prompt,
        )

        return task

    async def execute(self, task: Task) -> Task:
        task.status = TaskStatus.RUNNING

        logger.info("Task started | id=%s", task.id)

        try:
            # V0.2 çekirdeği.
            # Araştırmacı/developer/tester ajanları sonraki aşamalarda
            # bu pipeline'a bağlanacak.
            task.result = (
                f"NOXiA görevi aldı.\n\n"
                f"Görev ID: {task.id}\n"
                f"İstek: {task.prompt}"
            )

            task.status = TaskStatus.COMPLETED

        except Exception as exc:
            task.status = TaskStatus.FAILED
            task.error = str(exc)
            logger.exception("Task failed | id=%s", task.id)

        return task

    async def run(self, prompt: str, source: str = "telegram") -> Task:
        task = await self.create_task(prompt, source)
        return await self.execute(task)
