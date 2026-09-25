class TelegramUIManager:
    @staticmethod
    def get_main_menu_keyboard() -> dict:
        return {
            "keyboard": [
                [{"text": "🚀 Araştır"}, {"text": "💻 Geliştir"}],
                [{"text": "🧪 Test Et"}, {"text": "📋 Görevler"}],
                [{"text": "🧠 Hafıza"}, {"text": "📊 Sistem Durumu"}],
                [{"text": "⚙️ Ayarlar"}, {"text": "❓ Yardım"}]
            ],
            "resize_keyboard": True
        }

    @staticmethod
    def handle_command(command: str) -> dict:
        cmd = command.strip().lower()
        if cmd == "/start":
            return {"status": "success", "message": "NOXiA 2.0 Agent Platformuna hoş geldin! Sistem aktif ve hazır."}
        elif cmd == "/help":
            return {"status": "success", "message": "Yardım Menüsü: Araştırma, kod geliştirme, test etme ve otonom görevler için klavyeyi kullanabilirsin."}
        elif cmd == "/status":
            return {"status": "success", "message": "Sistem Durumu: Çekirdek aktif, tüm testler yeşil, veritabanı bağlı."}
        return {"status": "unknown", "message": "Bilinmeyen komut."}
