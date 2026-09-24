from pathlib import Path
import aiosqlite


async def initialize_memory(database_path: Path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)

    async with aiosqlite.connect(database_path) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                prompt TEXT NOT NULL,
                source TEXT NOT NULL,
                status TEXT NOT NULL,
                plan TEXT NOT NULL,
                result TEXT,
                error TEXT,
                created_at TEXT NOT NULL
            )
        """)

        await db.commit()


async def save_memory(
    database_path: Path,
    category: str,
    content: str,
) -> None:
    async with aiosqlite.connect(database_path) as db:
        await db.execute(
            """
            INSERT INTO memories (category, content)
            VALUES (?, ?)
            """,
            (category, content),
        )
        await db.commit()


async def search_memories(
    database_path: Path,
    query: str,
    limit: int = 10,
) -> list[tuple]:
    async with aiosqlite.connect(database_path) as db:
        cursor = await db.execute(
            """
            SELECT id, category, content, created_at
            FROM memories
            WHERE content LIKE ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (f"%{query}%", limit),
        )
        return await cursor.fetchall()


async def log_task(database_path: Path, task) -> None:
    async with aiosqlite.connect(database_path) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO tasks
            (id, prompt, source, status, plan, result, error, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                task.id,
                task.prompt,
                task.source,
                task.status.value,
                ",".join(task.plan),
                task.result,
                task.error,
                task.created_at.isoformat(),
            ),
        )
        await db.commit()
