import os
from pathlib import Path
from app.bot.service import BotService


class TelegramBotHandler:
    def __init__(self, database_path: Path, token: str = None):
        self.database_path = database_path
        self.token = token or os.getenv("TELEGRAM_BOT_TOKEN", "mock_token")
        self.service = BotService(database_path=database_path)

    async def process_incoming_message(self, chat_id: str, text: str) -> str:
        task_id = f"chat-{chat_id}"
        response = await self.service.handle_message(task_id, text)
        return response
