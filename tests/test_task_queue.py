import pytest
from app.core.task_queue import AsyncioTaskQueue

@pytest.mark.asyncio
async def test_asyncio_task_queue_workflow():
    tq = AsyncioTaskQueue()
    tq.enqueue("send_notification", {"chat_id": 123, "text": "Hello"})
    
    assert len(tq.queue) == 1
    
    processed = await tq.process_next()
    assert processed["status"] == "completed"
    assert processed["name"] == "send_notification"
    assert len(tq.queue) == 0
    assert len(tq.completed_tasks) == 1
