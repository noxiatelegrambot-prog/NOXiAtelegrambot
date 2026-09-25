from app.core.deployment_manager import DeploymentManager

def test_railway_config_generation():
    config = DeploymentManager.generate_railway_config()
    assert "build" in config
    assert config["deploy"]["startCommand"] == "python -m app.main"

def test_deployment_health_check():
    res_healthy = DeploymentManager.check_deployment_health(200)
    assert res_healthy["is_healthy"] is True

    res_unhealthy = DeploymentManager.check_deployment_health(503)
    assert res_unhealthy["is_healthy"] is False
