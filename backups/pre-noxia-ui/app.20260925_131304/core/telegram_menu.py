class TelegramMenuManager:
    @staticmethod
    def get_main_menu_keyboard() -> dict:
        # Define inline keyboard structure for NOXiA main menu
        return {
            "inline_keyboard": [
                [{"text": "🧠 Araştır", "callback_data": "menu_research"}, {"text": "💻 Geliştir", "callback_data": "menu_develop"}],
                [{"text": "🧪 Test", "callback_data": "menu_test"}, {"text": "📋 Görevler", "callback_data": "menu_tasks"}],
                [{"text": "🧠 Hafıza", "callback_data": "menu_memory"}, {"text": "📊 Durum", "callback_data": "menu_status"}],
                [{"text": "⚙️ Ayarlar", "callback_data": "menu_settings"}, {"text": "❓ Yardım", "callback_data": "menu_help"}]
            ]
        }

    @staticmethod
    def handle_callback(callback_data: str) -> dict:
        valid_actions = {
            "menu_research": "Research screen loaded.",
            "menu_develop": "Development screen loaded.",
            "menu_test": "Testing screen loaded.",
            "menu_tasks": "Tasks screen loaded.",
            "menu_memory": "Memory screen loaded.",
            "menu_status": "System status loaded.",
            "menu_settings": "Settings loaded.",
            "menu_help": "Help screen loaded."
        }
        response_text = valid_actions.get(callback_data, "Unknown menu action.")
        return {"status": "success", "message": response_text}
