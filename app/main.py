import logging
from pathlib import Path

import aiosqlite
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from app.brain.orchestrator import Orchestrator
from app.config import load_settings
from app.memory.database import initialize_memory


logger = logging.getLogger("noxia")


async def init_database(database_path: Path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)

    async with aiosqlite.connect(database_path) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await db.commit()

    await initialize_memory(database_path)


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    user = update.effective_user

    if user is None or update.message is None:
        return

    settings = context.application.bot_data["settings"]

    async with aiosqlite.connect(settings.database_path) as db:
        await db.execute(
            """
            INSERT INTO users (
                telegram_id,
                username,
                first_name
            )
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name
            """,
            (
                user.id,
                user.username,
                user.first_name,
            ),
        )
        await db.commit()

    await update.message.reply_text(
        "Merhaba! Ben NOXiA.\n\n"
        "Araştırma, öğrenme, geliştirme ve test sistemi "
        "aktif olarak kuruluyor.\n\n"
        "/help — Komutlar\n"
        "/status — Sistem durumu"
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None:
        return

    await update.message.reply_text(
        "NOXiA V0.2\n\n"
        "/start — Başlat\n"
        "/help — Yardım\n"
        "/status — Sistem durumu\n\n"
        "Normal mesaj göndererek NOXiA'ya görev verebilirsin."
    )


async def status_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None:
        return

    settings = context.application.bot_data["settings"]
    orchestrator = context.application.bot_data["orchestrator"]

    await update.message.reply_text(
        "NOXiA çalışıyor.\n\n"
        f"Environment: {settings.environment}\n"
        f"Aktif görevler: {len(orchestrator.active_tasks)}"
    )


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None or not update.message.text:
        return

    prompt = update.message.text.strip()

    if not prompt:
        return

    orchestrator: Orchestrator = (
        context.application.bot_data["orchestrator"]
    )

    task = await orchestrator.run(
        prompt,
        source="telegram",
    )

    await update.message.reply_text(
        task.result
        or "Görev işlendi fakat sonuç oluşturulamadı."
    )


async def post_init(application: Application) -> None:
    settings = application.bot_data["settings"]

    await init_database(settings.database_path)

    logger.info("Database and memory initialized")


def main() -> None:
    settings = load_settings()

    logging.basicConfig(
        level=getattr(
            logging,
            settings.log_level.upper(),
            logging.INFO,
        ),
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
    )

    orchestrator = Orchestrator()

    application = (
        Application.builder()
        .token(settings.telegram_bot_token)
        .post_init(post_init)
        .build()
    )

    application.bot_data["settings"] = settings
    application.bot_data["orchestrator"] = orchestrator

    application.add_handler(
        CommandHandler("start", start_command)
    )
    application.add_handler(
        CommandHandler("help", help_command)
    )
    application.add_handler(
        CommandHandler("status", status_command)
    )

    application.add_handler(
        __import__(
            "telegram.ext",
            fromlist=["MessageHandler"],
        ).MessageHandler(
            __import__(
                "telegram.ext",
                fromlist=["filters"],
            ).filters.TEXT
            & ~__import__(
                "telegram.ext",
                fromlist=["filters"],
            ).filters.COMMAND,
            message_handler,
        )
    )

    logger.info("NOXiA starting")
    application.run_polling()


if __name__ == "__main__":
    main()
