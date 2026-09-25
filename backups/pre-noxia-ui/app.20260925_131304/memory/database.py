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
                task_id TEXT,
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

        await db.execute("""
            CREATE TABLE IF NOT EXISTS agent_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT NOT NULL,
                agent TEXT NOT NULL,
                input_text TEXT NOT NULL,
                output_text TEXT,
                success INTEGER NOT NULL,
                duration_ms INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        await db.commit()


async def save_memory(
    database_path: Path,
    category: str,
    content: str,
    task_id: str | None = None,
) -> None:
    async with aiosqlite.connect(database_path) as db:
        await db.execute(
            """
            INSERT INTO memories (category, content, task_id)
            VALUES (?, ?, ?)
            """,
            (category, content, task_id),
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
            SELECT id, category, content, task_id, created_at
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


async def save_agent_run(
    database_path: Path,
    task_id: str,
    agent: str,
    input_text: str,
    output_text: str | None,
    success: bool,
    duration_ms: int | None = None,
) -> None:
    async with aiosqlite.connect(database_path) as db:
        await db.execute(
            """
            INSERT INTO agent_runs (
                task_id,
                agent,
                input_text,
                output_text,
                success,
                duration_ms
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                task_id,
                agent,
                input_text,
                output_text,
                int(success),
                duration_ms,
            ),
        )
        await db.commit()


async def get_agent_runs(
    database_path: Path,
    task_id: str,
) -> list[dict]:
    async with aiosqlite.connect(database_path) as db:
        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT
                id,
                task_id,
                agent,
                input_text,
                output_text,
                success,
                duration_ms,
                created_at
            FROM agent_runs
            WHERE task_id = ?
            ORDER BY id ASC
            """,
            (task_id,),
        )

        rows = await cursor.fetchall()

    return [
        {
            "id": row["id"],
            "task_id": row["task_id"],
            "agent": row["agent"],
            "input_text": row["input_text"],
            "output_text": row["output_text"],
            "success": bool(row["success"]),
            "duration_ms": row["duration_ms"],
            "created_at": row["created_at"],
        }
        for row in rows
    ]


async def save_experience(
    database_path: Path,
    task_id: str,
    situation: str,
    action: str,
    result: str,
    lesson: str,
    success: bool,
) -> None:
    async with aiosqlite.connect(database_path) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS experiences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT NOT NULL,
                situation TEXT NOT NULL,
                action TEXT NOT NULL,
                result TEXT NOT NULL,
                lesson TEXT NOT NULL,
                success INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        await db.execute(
            """
            INSERT INTO experiences (
                task_id,
                situation,
                action,
                result,
                lesson,
                success
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                task_id,
                situation,
                action,
                result,
                lesson,
                int(success),
            ),
        )

        await db.commit()


async def get_experiences(
    database_path: Path,
    task_id: str | None = None,
    limit: int = 20,
) -> list[dict]:
    async with aiosqlite.connect(database_path) as db:
        db.row_factory = aiosqlite.Row

        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS experiences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT NOT NULL,
                situation TEXT NOT NULL,
                action TEXT NOT NULL,
                result TEXT NOT NULL,
                lesson TEXT NOT NULL,
                success INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        if task_id is not None:
            cursor = await db.execute(
                """
                SELECT
                    id,
                    task_id,
                    situation,
                    action,
                    result,
                    lesson,
                    success,
                    created_at
                FROM experiences
                WHERE task_id = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (task_id, limit),
            )
        else:
            cursor = await db.execute(
                """
                SELECT
                    id,
                    task_id,
                    situation,
                    action,
                    result,
                    lesson,
                    success,
                    created_at
                FROM experiences
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            )

        rows = await cursor.fetchall()

        return [
            {
                "id": row["id"],
                "task_id": row["task_id"],
                "situation": row["situation"],
                "action": row["action"],
                "result": row["result"],
                "lesson": row["lesson"],
                "success": bool(row["success"]),
                "created_at": row["created_at"],
            }
            for row in rows
        ]

async def search_experiences(db_path: str, query: str, limit: int = 5) -> list[dict]:
    """
    Search experiences using simple keyword/LIKE matching on situation, lesson, or action.
    """
    import aiosqlite
    keywords = [kw.strip() for kw in query.split() if kw.strip()]
    if not keywords:
        return []

    async with aiosqlite.connect(db_path) as db:
        db.row_factory = aiosqlite.Row
        conditions = []
        params = []
        for kw in keywords:
            conditions.append("(situation LIKE ? OR lesson LIKE ? OR action LIKE ?)")
            pattern = f"%{kw}%"
            params.extend([pattern, pattern, pattern])
        
        where_clause = " OR ".join(conditions)
        sql = f"SELECT * FROM experiences WHERE {where_clause} ORDER BY created_at DESC LIMIT ?"
        params.append(limit)

        async with db.execute(sql, params) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_memories(database_path: Path, task_id: str) -> list:
    async with aiosqlite.connect(database_path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM memories WHERE task_id = ? ORDER BY id ASC", (task_id,)
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_system_metrics(database_path: Path) -> dict:
    async with aiosqlite.connect(database_path) as db:
        async with db.execute("SELECT COUNT(*) FROM memories") as cursor:
            mem_count = (await cursor.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM agent_runs") as cursor:
            runs_count = (await cursor.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM agent_runs WHERE success = 1") as cursor:
            success_count = (await cursor.fetchone())[0]
        return {
            "total_memories": mem_count,
            "total_runs": runs_count,
            "successful_runs": success_count,
            "success_rate": (success_count / runs_count * 100) if runs_count > 0 else 0.0
        }
