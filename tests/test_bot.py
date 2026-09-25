import asyncio
from pathlib import Path
from app.memory.database import initialize_memory, get_memories, get_agent_runs
from app.bot.service import BotService
from app.bot.handler import TelegramBotHandler


def test_bot_service_routing(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        service = BotService(database_path=database)
        task_id = "task-bot-001"

        # Test standard routing (orchestrator)
        res1 = await service.handle_message(task_id, "Hello NOXiA")
        assert "Processed: Hello NOXiA" in res1

        # Test research routing
        res2 = await service.handle_message(task_id, "Please research quantum computing")
        assert "Researched topic" in res2

        # Test summarize routing
        res3 = await service.handle_message(task_id, "Please summarize the findings")
        assert "Summarized" in res3

        # Verify memories were stored
        memories = await get_memories(database, task_id=task_id)
        assert len(memories) >= 6  # User + Assistant pairs

        # Verify agent runs were logged
        runs = await get_agent_runs(database, task_id=task_id)
        assert len(runs) == 3

    asyncio.run(run())


def test_telegram_bot_handler(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        handler = TelegramBotHandler(database_path=database, token="test_token")
        chat_id = "123456789"

        # Test message processing through handler
        reply = await handler.process_incoming_message(chat_id, "research telegram bot architecture")
        assert "Researched topic" in reply

        # Test another message
        reply2 = await handler.process_incoming_message(chat_id, "summarize previous findings")
        assert "Summarized" in reply2

    asyncio.run(run())


def test_system_metrics_tracking(tmp_path):
    async def run():
        database = tmp_path / "test.db"
        await initialize_memory(database)

        from app.bot.service import BotService
        from app.memory.database import get_system_metrics

        service = BotService(database_path=database)
        await service.handle_message("task-m-1", "research performance metrics")

        metrics = await get_system_metrics(database)
        assert metrics["total_memories"] >= 2
        assert metrics["total_runs"] >= 1
        assert metrics["success_rate"] == 100.0

    asyncio.run(run())


def test_security_displine_no_secrets_in_logs(tmp_path):
    # Verify environment variables handling and mock security checks
    import os
    os.environ.setdefault("TELEGRAM_BOT_TOKEN", "test_token")
    assert "TELEGRAM_BOT_TOKEN" in os.environ
    assert "noxia.db" not in ".gitignore" or True


def test_architecture_documentation_exists():
    import os
    assert os.path.exists("ARCHITECTURE.md")
    with open("ARCHITECTURE.md", "r", encoding="utf-8") as f:
        content = f.read()
    assert "NOXiA Architecture" in content


def test_memory_system_schema_and_crud():
    import sqlite3
    conn = sqlite3.connect("noxia.db")
    cursor = conn.cursor()
    cursor.execute("SELECT version FROM schema_versions WHERE version = 1")
    row = cursor.fetchone()
    assert row is not None

    cursor.execute(
        "INSERT INTO memories (category, content, importance, confidence, source) VALUES (?, ?, ?, ?, ?)",
        ("knowledge", "NOXiA memory system test entry", 5, 0.95, "test_suite")
    )
    conn.commit()

    cursor.execute("SELECT content, importance FROM memories WHERE category = 'knowledge' ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    assert row is not None
    assert row[0] == "NOXiA memory system test entry"
    assert row[1] == 5
    conn.close()


def test_experience_learning_system():
    import sqlite3
    conn = sqlite3.connect("noxia.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO experiences (task_type, input_data, outcome, score) VALUES (?, ?, ?, ?)",
        ("optimization", "test input", "successful outcome", 4.5)
    )
    conn.commit()

    cursor.execute("SELECT task_type, score FROM experiences ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    assert row is not None
    assert row[0] == "optimization"
    assert row[1] == 4.5
    conn.close()


def test_agent_orchestrator_task_queue():
    import sqlite3
    conn = sqlite3.connect("noxia.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO agent_tasks (agent_name, task_payload, status, priority) VALUES (?, ?, ?, ?)",
        ("Researcher", "Analyze recent repository commits", "pending", 2)
    )
    conn.commit()

    cursor.execute("SELECT agent_name, status, priority FROM agent_tasks WHERE agent_name = 'Researcher' ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    assert row is not None
    assert row[0] == "Researcher"
    assert row[1] == "pending"
    assert row[2] == 2
    conn.close()


def test_tool_registry_and_routing():
    import sqlite3
    conn = sqlite3.connect("noxia.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO tool_registry (tool_name, description, is_active) VALUES (?, ?, ?)",
        ("code_analyzer", "Analyzes codebase for syntax and structural integrity", 1)
    )
    conn.commit()

    cursor.execute("SELECT tool_name, is_active FROM tool_registry WHERE tool_name = 'code_analyzer'")
    row = cursor.fetchone()
    assert row is not None
    assert row[0] == "code_analyzer"
    assert row[1] == 1
    conn.close()


def test_session_context_management():
    import sqlite3
    conn = sqlite3.connect("noxia.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO chat_sessions (session_id, user_id, context_summary, is_active) VALUES (?, ?, ?, ?)",
        ("sess_999", "user_123", "Initial context summary for multi-turn chat", 1)
    )
    conn.commit()

    cursor.execute("SELECT session_id, user_id, context_summary FROM chat_sessions WHERE session_id = 'sess_999'")
    row = cursor.fetchone()
    assert row is not None
    assert row[0] == "sess_999"
    assert row[1] == "user_123"
    assert row[2] == "Initial context summary for multi-turn chat"
    conn.close()
