class DeploymentManager:
    @staticmethod
    def generate_railway_config() -> dict:
        return {
            "build": {"builder": "NIXPACKS"},
            "deploy": {
                "startCommand": "python -m app.main",
                "restartPolicyType": "ON_FAILURE",
                "restartPolicyMaxRetries": 3
            }
        }

    @staticmethod
    def check_deployment_health(status_code: int) -> dict:
        is_healthy = status_code == 200
        return {
            "status": "success",
            "is_healthy": is_healthy,
            "http_status": status_code,
            "message": "Deployment is live and responding normally." if is_healthy else "Deployment health check failed or service unavailable."
        }
