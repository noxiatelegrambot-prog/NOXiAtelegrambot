import subprocess

class TestAgent:
    @staticmethod
    def run_tests_in_sandbox(sandbox_path: str) -> dict:
        try:
            result = subprocess.run(
                ["python3", "-m", "pytest", "-q"],
                cwd=sandbox_path,
                capture_output=True,
                text=True,
                timeout=15
            )
            passed = result.returncode == 0
            return {
                "status": "success",
                "tests_passed": passed,
                "exit_code": result.returncode,
                "output": result.stdout + result.stderr
            }
        except Exception as e:
            return {
                "status": "error",
                "tests_passed": False,
                "output": str(e)
            }
