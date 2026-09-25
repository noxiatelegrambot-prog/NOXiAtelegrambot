import asyncio
import os
from pathlib import Path
from app.memory.database import initialize_memory
from app.bot.handler import TelegramBotHandler


async def main():
    database_path = Path("noxia.db")
    await initialize_memory(database_path)
    
    token = os.getenv("TELEGRAM_BOT_TOKEN", "mock_token")
    handler = TelegramBotHandler(database_path=database_path, token=token)
    
    print(f"NOXiA Autonomous Multi-Agent System initialized. Bot token: {token[:4]}... [Running in mock/polling mode]")

if __name__ == "__main__":
    asyncio.run(main())
