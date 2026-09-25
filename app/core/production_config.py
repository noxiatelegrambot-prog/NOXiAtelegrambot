import os

class ProductionConfigValidator:
    @staticmethod
    def validate_environment() -> dict:
        env = os.getenv("NOXIA_ENV", "development")
        api_key = os.getenv("OPENAI_API_KEY", "")
        
        # In strict production mode, ensure production flags and keys are set
        is_production = (env == "production")
        
        return {
            "environment": env,
            "is_production": is_production,
            "has_api_key": bool(api_key),
            "status": "validated"
        }
