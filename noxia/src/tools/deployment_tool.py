import subprocess

class DeploymentTool:
    @staticmethod
    def check_railway_status() -> dict:
        try:
            result = subprocess.run(
                ["railway", "status"],
                capture_output=True,
                text=True
            )
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": "Railway CLI kurulu değil veya yapılandırılmamış."
            }
