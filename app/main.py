import logging
from pathlib import Path

import aiosqlite
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from app.ai.providers import AIRouter
from app.brain.orchestrator import Orchestrator
from app.config import load_settings
from app.memory.database import initialize_memory
from app.ui.keyboards import get_complete_main_dashboard_keyboard
from app.core.intent_transmuter import IntentTransmuter
from app.core.dialogue_engine import DialogueEngine
from app.core.intent_transmuter import IntentTransmuter
from app.core.dialogue_engine import DialogueEngine


logger = logging.getLogger("noxia")
intent_router = IntentTransmuter()
dialogue_engine = DialogueEngine()


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


def main_keyboard() -> InlineKeyboardMarkup:
    return get_complete_main_dashboard_keyboard()

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

    context.user_data["mode"] = "task"

    await update.message.reply_text(
        "⚡ NOXiA\n\n"
        "Görev merkezine hoş geldin.\n"
        "Aşağıdan bir çalışma modu seç veya doğrudan görevini yaz.",
        reply_markup=main_keyboard(),
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None:
        return

    await update.message.reply_text(
        "⚡ NOXiA Yardım\n\n"
        "🔎 Araştır — web araştırması\n"
        "💻 Geliştir — kontrollü kod değişikliği\n"
        "🧪 Test Et — gerçek test çalıştırma\n"
        "🤖 Genel Görev — planner tarafından belirlenir\n\n"
        "/start — ana menü\n"
        "/status — sistem durumu\n"
        "/help — yardım",
        reply_markup=main_keyboard(),
    )


async def status_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None:
        return

    router: AIRouter = context.application.bot_data["ai_router"]
    orchestrator = context.application.bot_data["orchestrator"]

    status = router.status()

    lines = [
        "⚙️ NOXiA Sistem Durumu",
        "",
        f"Aktif görevler: {len(orchestrator.active_tasks)}",
        "",
        "🧠 AI Provider'ları:",
    ]

    for name, info in status.items():
        state = "🟢 hazır" if info["configured"] else "⚪ anahtar yok"
        lines.append(
            f"{name}: {state} — {info['model']}"
        )

    lines.extend(
        [
            "",
            "Fallback sırası:",
            " → ".join(router.configured()),
        ]
    )

    await update.message.reply_text(
        "\n".join(lines),
        reply_markup=main_keyboard(),
    )


async def callback_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = update.callback_query

    if query is None:
        return

    await query.answer()

    data = query.data or ""

    if data.startswith("mode:"):
        mode = data.split(":", 1)[1]
        context.user_data["mode"] = mode

        labels = {
            "research": "🔎 Araştırma modu aktif.\n\nAraştırmak istediğin konuyu yaz.",
            "develop": "💻 Geliştirme modu aktif.\n\nYapılmasını istediğin kontrollü değişikliği yaz.",
            "test": "🧪 Test modu aktif.\n\nÇalıştırılmasını istediğin testi veya kontrolü yaz.",
            "task": "🤖 Genel görev modu aktif.\n\nGörevini yaz.",
        }

        await query.edit_message_text(
            labels.get(mode, "Görev modunu seç."),
            reply_markup=main_keyboard(),
        )
        return

    if data == "status:ai":
        router: AIRouter = context.application.bot_data["ai_router"]
        status = router.status()

        lines = ["🧠 AI Provider Durumu", ""]

        for name, info in status.items():
            state = "🟢" if info["configured"] else "⚪"
            lines.append(
                f"{state} {name} — {info['model']}"
            )

        lines.extend(
            [
                "",
                "Fallback:",
                " → ".join(router.configured()),
            ]
        )

        await query.edit_message_text(
            "\n".join(lines),
            reply_markup=main_keyboard(),
        )
        return

    if data == "status:system":
        orchestrator = context.application.bot_data["orchestrator"]

        await query.edit_message_text(
            "⚙️ Sistem\n\n"
            "🟢 Telegram: aktif\n"
            "🟢 Orchestrator: aktif\n"
            f"📋 Aktif görev: {len(orchestrator.active_tasks)}",
            reply_markup=main_keyboard(),
        )


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None or not update.message.text:
        return

    raw_prompt = update.message.text.strip()
    if not raw_prompt:
        return

    transmuter: IntentTransmuter = (
        context.application.bot_data["intent_transmuter"]
    )
    dialogue: DialogueEngine = (
        context.application.bot_data["dialogue_engine"]
    )

    intent = transmuter.transmute(raw_prompt)
    intent_type = intent.get("intent", "task")

    # Öğrenme mesajı: "Öğren: tetikleyici -> cevap"
    if intent_type == "learn":
        body = raw_prompt.split(":", 1)[1].strip()
        if "->" in body:
            trigger, response = body.split("->", 1)
            trigger = trigger.strip()
            response = response.strip()

            if trigger and response:
                dialogue.learn_response(trigger, response)
                await update.message.reply_text(
                    f"🧠 Öğrenildi.\n\n"
                    f"🔑 Tetikleyici: {trigger}\n"
                    f"💬 Yanıt: {response}",
                    reply_markup=main_keyboard(),
                )
                return

        await update.message.reply_text(
            "🧠 Öğrenme formatı:\n\n"
            "Öğren: merhaba -> Selam! Nasılsın?",
            reply_markup=main_keyboard(),
        )
        return

    # Normal sohbet: Orchestrator'a görev oluşturma.
    if intent_type == "chat":
        user = update.effective_user
        user_id = user.id if user else 0

        response = dialogue.generate_response(
            user_id,
            raw_prompt,
        )

        await update.message.reply_text(
            response,
            reply_markup=main_keyboard(),
        )
        return

    # Sadece gerçek görevler Orchestrator'a gider.
    intent = intent_router.transmute(prompt)
    logger.info("Intent routed | intent=%s | action=%s | confidence=%s",
                intent.get("intent"), intent.get("transmuted_action"),
                intent.get("confidence"))

    if intent.get("intent") == "chat":
        user_id = update.effective_user.id if update.effective_user else 0
        response = dialogue_engine.generate_response(user_id, prompt)
        await update.message.reply_text(response, reply_markup=main_keyboard())
        return

    if intent.get("intent") == "learn":
        await update.message.reply_text(
            "🧠 Öğrenme isteği algılandı. Öğrenme sistemi devrede.",
            reply_markup=main_keyboard(),
        )
        return

    mode = context.user_data.get("mode", "task")

    prefixes = {
        "research": "[RESEARCH MODE]",
        "develop": "[DEVELOP MODE]",
        "test": "[TEST MODE]",
        "task": "[GENERAL TASK]",
    }

    prompt = f"{prefixes.get(mode, '[GENERAL TASK]')} {raw_prompt}"

    orchestrator: Orchestrator = (
        context.application.bot_data["orchestrator"]
    )

    await update.message.chat.send_action("typing")

    task = await orchestrator.run(
        prompt,
        source="telegram",
    )

    if task.status.value == "failed":
        result = (
            "❌ Görev başarısız.\n\n"
            f"{task.error or 'Bilinmeyen hata.'}"
        )
    else:
        result = (
            "✅ Görev tamamlandı.\n\n"
            + (
                task.result
                or "Görev işlendi fakat sonuç oluşturulamadı."
            )
        )

    await update.message.reply_text(
        result,
        reply_markup=main_keyboard(),
    )

async def register_noxia_commands(application: Application) -> None:
    await application.bot.set_my_commands([
        ("NOXiA_start", "NOXiA ana menüyü aç"),
        ("NOXiA_help", "NOXiA yardım"),
        ("NOXiA_status", "NOXiA sistem durumu"),
    ])


async def post_init(application: Application) -> None:
    await register_noxia_commands(application)
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

    orchestrator = Orchestrator(
        database_path=settings.database_path
    )

    ai_router = AIRouter()
    intent_transmuter = IntentTransmuter()
    dialogue_engine = DialogueEngine()

    application = (
        Application.builder()
        .token(settings.telegram_bot_token)
        .post_init(post_init)
        .build()
    )

    application.bot_data["settings"] = settings
    application.bot_data["orchestrator"] = orchestrator
    application.bot_data["ai_router"] = ai_router
    application.bot_data["intent_transmuter"] = intent_transmuter
    application.bot_data["dialogue_engine"] = dialogue_engine

    application.add_handler(
        CommandHandler("NOXiA_start", start_command)
    )

    application.add_handler(
        CommandHandler("NOXiA_help", help_command)
    )

    application.add_handler(
        CommandHandler("NOXiA_status", status_command)
    )

    application.add_handler(
        CallbackQueryHandler(callback_handler)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )

    logger.info("NOXiA starting")
    application.run_polling()


if __name__ == "__main__":
    main()
