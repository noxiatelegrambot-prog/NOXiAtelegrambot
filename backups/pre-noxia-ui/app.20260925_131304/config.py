import os
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    database_path: Path
    environment: str
    log_level: str


def load_settings() -> Settings:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

    database_path = Path(
        os.getenv("DATABASE_PATH", str(BASE_DIR / "data" / "noxia.db"))
    )

    return Settings(
        telegram_bot_token=token,
        database_path=database_path,
        environment=os.getenv("NOXIA_ENV", "development"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
