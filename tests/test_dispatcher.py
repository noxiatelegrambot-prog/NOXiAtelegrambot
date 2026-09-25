
from app.core.dispatcher import TelegramDispatcher

def test_telegram_dispatcher_auth_and_routing():
    dispatcher = TelegramDispatcher(allowed_user_ids=[12345])
    
    # Register test handler
    dispatcher.register_handler("/start", lambda p: "Welcome to NOXiA 2.0")

    # Unauthorized test
    res_unauth = dispatcher.dispatch(99999, "/start")
    assert res_unauth["status"] == "unauthorized"

    # Authorized test
    res_auth = dispatcher.dispatch(12345, "/start")
    assert res_auth["status"] == "success"
    assert "NOXiA 2.0" in res_auth["response"]

    # Unknown command test
    res_unknown = dispatcher.dispatch(12345, "/unknown")
    assert res_unknown["status"] == "not_found"
