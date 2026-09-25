from app.core.telegram_menu import TelegramMenuManager

def test_main_menu_keyboard():
    keyboard = TelegramMenuManager.get_main_menu_keyboard()
    assert "inline_keyboard" in keyboard
    assert len(keyboard["inline_keyboard"]) == 4

def test_menu_callbacks():
    res = TelegramMenuManager.handle_callback("menu_research")
    assert res["status"] == "success"
    assert "Research" in res["message"]

    invalid_res = TelegramMenuManager.handle_callback("invalid_action")
    assert invalid_res["status"] == "success"
    assert "Unknown" in invalid_res["message"]
