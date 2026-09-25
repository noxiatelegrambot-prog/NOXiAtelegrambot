from app.core.game_handlers import GameHandlers

def test_bulmaca_handler():
    res = GameHandlers.handle_bulmaca_command()
    assert res["status"] == "success"
    assert "Kelime Bulmaca" in res["text"]
    assert "original" in res

def test_liderlik_handler():
    text = GameHandlers.handle_liderlik_command()
    assert "Liderlik Tablosu" in text
