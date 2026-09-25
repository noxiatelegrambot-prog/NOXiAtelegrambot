from app.core.noxia_registry import NoxiaRegistry

class CommandRegistrar:
    @staticmethod
    def get_telegram_commands_payload() -> list:
        # Telegram API bot commands list format
        return [
            {"command": NoxiaRegistry.COMMANDS["start"], "description": "🧠 NOXiA Ana Menüyü Aç"},
            {"command": NoxiaRegistry.COMMANDS["help"], "description": "❓ Yardım ve Komut Listesi"},
            {"command": NoxiaRegistry.COMMANDS["status"], "description": "📊 Anlık Sistem Durumu"},
            {"command": NoxiaRegistry.COMMANDS["settings"], "description": "⚙️ Bot Ayarları"},
            {"command": NoxiaRegistry.COMMANDS["task"], "description": "📋 Otonom Görev Yönetimi"},
            {"command": NoxiaRegistry.COMMANDS["bulmaca"], "description": "🔤 Kelime Bulmaca Oyunu Başlat"},
            {"command": NoxiaRegistry.COMMANDS["liderlik"], "description": "🏆 Grup Liderlik Tablosu"},
        ]

    @staticmethod
    def format_command_menu_text() -> str:
        payload = CommandRegistrar.get_telegram_commands_payload()
        text = "📋 **NOXiA Komut Listesi (Menu / A)**\n\n"
        for cmd in payload:
            text += f"/{cmd['command']} — {cmd['description']}\n"
        return text
