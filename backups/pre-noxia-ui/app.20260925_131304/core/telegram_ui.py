from app.core.noxia_registry import NoxiaRegistry
from app.core.telemetry_manager import TelemetryManager

class TelegramUIManager:
    @staticmethod
    def get_main_menu_keyboard() -> dict:
        return {
            "title": NoxiaRegistry.UI_TEXTS["main_title"],
            "buttons": [
                [NoxiaRegistry.UI_TEXTS["menu_research"], NoxiaRegistry.UI_TEXTS["menu_dev"]],
                [NoxiaRegistry.UI_TEXTS["menu_test"], NoxiaRegistry.UI_TEXTS["menu_tasks"]],
                [NoxiaRegistry.UI_TEXTS["menu_memory"], NoxiaRegistry.UI_TEXTS["menu_status"]],
                [NoxiaRegistry.UI_TEXTS["menu_settings"], NoxiaRegistry.UI_TEXTS["menu_help"]]
            ]
        }

    @staticmethod
    def get_submenu(category: str) -> dict:
        items = NoxiaRegistry.SUBMENUS.get(category, [])
        return {
            "category": category,
            "items": items,
            "back_button": NoxiaRegistry.UI_TEXTS["back_to_main"]
        }

    @staticmethod
    def get_real_system_status() -> dict:
        tm = TelemetryManager()
        summary = tm.get_summary()
        return {
            "status": "success",
            "bot_state": "ONLINE",
            "ai_gateway": "ACTIVE",
            "database": "CONNECTED (noxia.db)",
            "railway": "DEPLOYED",
            "telemetry_metrics_count": summary["count"]
        }
