from app.core.telegram_ui import TelegramUIManager

def test_main_menu_structure():
    menu = TelegramUIManager.get_main_menu_keyboard()
    assert "NOXiA" in menu["title"]
    assert len(menu["buttons"]) == 4

def test_submenu_retrieval():
    sub = TelegramUIManager.get_submenu("dev")
    assert sub["category"] == "dev"
    assert "Yeni Geliştirme" in sub["items"]
    assert sub["back_button"] == "🔙 Ana Menü"

def test_real_system_status_integration():
    status = TelegramUIManager.get_real_system_status()
    assert status["status"] == "success"
    assert status["bot_state"] == "ONLINE"
    assert "noxia.db" in status["database"]
