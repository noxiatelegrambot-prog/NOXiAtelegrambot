from app.core.health_check import ProductionHealthCheck

def test_production_health_check():
    hc = ProductionHealthCheck()
    status = hc.check_system_health()

    assert status["status"] == "healthy"
    assert status["services"]["database"] is True

    hc.toggle_service("database", False)
    degraded = hc.check_system_health()
    assert degraded["status"] == "degraded"
    assert degraded["services"]["database"] is False
