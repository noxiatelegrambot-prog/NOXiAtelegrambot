class UIStateRouter:
    @staticmethod
    def render_screen(screen_id: str, context: dict = None) -> dict:
        screens = {
            "main": {"title": "🧠 NOXiA Ana Ekran", "options": ["Araştır", "Geliştir", "Test", "Görevler"]},
            "research": {"title": "🔍 Araştır Ekranı", "input_prompt": "Araştırma konusunu girin:"},
            "develop": {"title": "💻 Geliştir Ekranı", "input_prompt": "Geliştirme talebini girin:"},
            "test": {"title": "🧪 Test Ekranı", "status": "Ready for execution"},
            "tasks": {"title": "📋 Görevler Ekranı", "active_tasks": context.get("active_tasks", []) if context else []},
            "memory": {"title": "🧠 Hafıza Ekranı", "status": "Active memory loaded"},
            "status": {"title": "📊 Sistem Durumu", "health": "Healthy"},
            "settings": {"title": "⚙️ Ayarlar Ekranı", "config": "Production Safe"}
        }
        
        screen = screens.get(screen_id, {"title": "Bilinmeyen Ekran"})
        return {"status": "success", "screen": screen_id, "content": screen}
