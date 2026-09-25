from app.core.noxia_registry import NoxiaRegistry
from app.core.command_registrar import CommandRegistrar
from app.core.game_handlers import GameHandlers
from app.core.social_suite import SocialSuiteManager
from app.core.daily_rewards import DailyRewardsManager
from app.core.telegram_ui import TelegramUIManager

class BotDispatcher:
    @staticmethod
    def route_command(command: str, user_id: int = 123, username: str = "test_user") -> dict:
        # Clean leading slash if present
        cmd_clean = command.lstrip("/").strip()
        
        if cmd_clean == NoxiaRegistry.COMMANDS["start"]:
            menu = TelegramUIManager.get_main_menu_keyboard()
            return {
                "route": "start",
                "text": f"🧠 **{menu['title']}**\n\nHoş geldin! Aşağıdaki menüden veya komutlardan dilediğin işlemi seçebilirsin.",
                "buttons": menu["buttons"]
            }
            
        elif cmd_clean == NoxiaRegistry.COMMANDS["help"]:
            menu_text = CommandRegistrar.format_command_menu_text()
            return {
                "route": "help",
                "text": menu_text
            }
            
        elif cmd_clean == NoxiaRegistry.COMMANDS["status"]:
            status = TelegramUIManager.get_real_system_status()
            return {
                "route": "status",
                "text": f"📊 **Sistem Durumu**\n\n• Durum: `{status['bot_state']}`\n• AI Gateway: `{status['ai_gateway']}`\n• Database: `{status['database']}`\n• Railway: `{status['railway']}`"
            }
            
        elif cmd_clean == NoxiaRegistry.COMMANDS["bulmaca"]:
            res = GameHandlers.handle_bulmaca_command()
            return {
                "route": "bulmaca",
                "text": res["text"]
            }
            
        elif cmd_clean == NoxiaRegistry.COMMANDS["liderlik"]:
            text = GameHandlers.handle_liderlik_command()
            return {
                "route": "liderlik",
                "text": text
            }
            
        else:
            personality = SocialSuiteManager.get_personality_response("error")
            return {
                "route": "unknown",
                "text": f"Bilinmeyen komut! {personality}"
            }
