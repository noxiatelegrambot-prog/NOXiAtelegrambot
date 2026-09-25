from app.core.bot_dispatcher import BotDispatcher
from app.core.noxia_registry import NoxiaRegistry

def test_dispatcher_start():
    res = BotDispatcher.route_command("/noxia_start", 999, "boss")
    assert res["route"] == "start"
    assert "NOXiA" in res["text"]
    assert len(res["buttons"]) > 0

def test_dispatcher_bulmaca():
    res = BotDispatcher.route_command("noxia_bulmaca", 999, "boss")
    assert res["route"] == "bulmaca"
    assert "Kelime Bulmaca" in res["text"]

def test_dispatcher_unknown():
    res = BotDispatcher.route_command("/gecersiz_komut", 999, "boss")
    assert res["route"] == "unknown"
    assert "Fatoş" in res["text"] or "hat" in res["text"] or "Sistem" in res["text"]
