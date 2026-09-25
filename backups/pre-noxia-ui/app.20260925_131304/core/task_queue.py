import asyncio

class AsyncioTaskQueue:
    def __init__(self):
        self.queue = []
        self.completed_tasks = []

    def enqueue(self, task_name: str, payload: dict) -> dict:
        task_item = {
            "id": len(self.queue) + len(self.completed_tasks) + 1,
            "name": task_name,
            "payload": payload,
            "status": "pending"
        }
        self.queue.append(task_item)
        return task_item

    async def process_next(self) -> dict:
        if not self.queue:
            return None
        
        task = self.queue.pop(0)
        task["status"] = "processing"
        
        # Simulate async work
        await asyncio.sleep(0.01)
        
        task["status"] = "completed"
        self.completed_tasks.append(task)
        return task
