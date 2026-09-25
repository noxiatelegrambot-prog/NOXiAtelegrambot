import subprocess

class TestingTool:
    @staticmethod
    def run_pytest() -> dict:
        try:
            result = subprocess.run(
                ["pytest"],
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
                "error": str(e)
            }
