from app.core.telegram_ui import TelegramUIManager

def test_main_menu_keyboard():
    kb = TelegramUIManager.get_main_menu_keyboard()
    assert "keyboard" in kb
    assert len(kb["keyboard"]) == 4

def test_telegram_commands():
    start = TelegramUIManager.handle_command("/start")
    assert start["status"] == "success"
    assert "hoş geldin" in start["message"]

    status = TelegramUIManager.handle_command("/status")
    assert status["status"] == "success"
    assert "Sistem Durumu" in status["message"]
