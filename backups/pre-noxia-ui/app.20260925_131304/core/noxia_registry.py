class NoxiaRegistry:
    # 1. STANDARDIZED COMMANDS (No conflict with other bots)
    COMMANDS = {
        "start": "noxia_start",
        "help": "noxia_help",
        "status": "noxia_status",
        "settings": "noxia_settings",
        "task": "noxia_task",
        "bulmaca": "noxia_bulmaca",
        "liderlik": "noxia_liderlik",
    }

    # 2. CALLBACK IDS & UI TEXTS
    UI_TEXTS = {
        "main_title": "🧠 NOXiA — Autonomous Agent Platform",
        "menu_research": "🔍 Araştır",
        "menu_dev": "💻 Geliştir",
        "menu_test": "🧪 Test",
        "menu_tasks": "📋 Görevler",
        "menu_memory": "🧠 Hafıza",
        "menu_status": "📊 Sistem Durumu",
        "menu_settings": "⚙️ Ayarlar",
        "menu_help": "❓ Yardım",
        "back_to_main": "🔙 Ana Menü"
    }

    # 3. SUBMENUS HIERARCHY
    SUBMENUS = {
        "research": ["Yeni Araştırma", "Aktif Araştırmalar", "Araştırma Geçmişi"],
        "dev": ["Yeni Geliştirme", "Aktif Görevler", "Geliştirme Geçmişi"],
        "test": ["Yeni Test", "Aktif Testler", "Test Geçmişi"],
        "tasks": ["Aktif", "Bekleyen", "Tamamlanan", "Başarısız"],
        "memory": ["Hafızayı Gör", "Ara", "Temizle"],
        "status": ["Bot", "AI", "Database", "Railway", "Agents"],
        "settings": ["Model", "Bildirimler", "Kullanıcı Ayarları"],
        "help": ["Komutlar", "NOXiA Nasıl Çalışır?", "Sistem Hakkında"]
    }

    @classmethod
    def get_command(cls, name: str) -> str:
        return cls.COMMANDS.get(name, f"noxia_{name}")
