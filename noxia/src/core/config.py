import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    PROJECT_NAME: str = "NOXiA Autonomous Platform"
    VERSION: str = "1.0.0"
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o")
    DB_PATH: str = os.getenv("DB_PATH", str(BASE_DIR / "noxia.db"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

settings = Settings()
