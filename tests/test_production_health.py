from app.core.production_health import ProductionHealthCheck

def test_production_health_check():
    health = ProductionHealthCheck.run_startup_check()
    assert health["status"] == "healthy"
    assert health["startup_probe"] == "passed"
    assert health["smoke_test"] == "passed"
    assert health["database_connected"] is True
