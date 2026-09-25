from app.core.production_guard import ProductionGuard

def test_production_env_verification():
    mock_env = {
        "OPENAI_API_KEY": "sk-mock-key",
        "TELEGRAM_BOT_TOKEN": "mock-token"
    }
    res = ProductionGuard.verify_environment(mock_env)
    assert res["status"] == "success"
    assert res["production_ready"] is True

def test_production_env_missing_secrets():
    mock_env = {}
    res = ProductionGuard.verify_environment(mock_env)
    assert res["status"] == "failed"
    assert "OPENAI_API_KEY" in res["missing_secrets"]

def test_health_check():
    hc = ProductionGuard.health_check()
    assert hc["status"] == "healthy"
    assert hc["smoke_test"] == "passed"
