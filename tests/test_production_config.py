from app.core.production_config import ProductionConfigValidator
import os

def test_production_config():
    # Test default/fallback behavior
    config = ProductionConfigValidator.validate_environment()
    assert config["status"] == "validated"
    assert "environment" in config
    assert "has_api_key" in config
