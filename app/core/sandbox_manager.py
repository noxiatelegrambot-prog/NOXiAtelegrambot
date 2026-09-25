import os
import shutil
import subprocess

class SandboxManager:
    @staticmethod
    def create_sandbox(task_id: str) -> dict:
        sandbox_path = f"/tmp/noxia_sandbox_{task_id}"
        os.makedirs(sandbox_path, exist_ok=True)
        return {
            "status": "success",
            "task_id": task_id,
            "sandbox_path": sandbox_path,
            "isolation": "filesystem_and_env"
        }

    @staticmethod
    def execute_command_in_sandbox(sandbox_path: str, command: list, timeout: int = 10) -> dict:
        denylist = ["rm -rf /", "mkfs", ":(){ :|:& };:"]
        cmd_str = " ".join(command)
        if any(bad in cmd_str for bad in denylist):
            return {"status": "blocked", "error": "Command violates security denylist"}

        try:
            result = subprocess.run(
                command,
                cwd=sandbox_path,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return {
                "status": "success",
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except subprocess.TimeoutExpired:
            return {"status": "failed", "error": "Sandbox execution timed out"}
        except Exception as e:
            return {"status": "failed", "error": str(e)}

    @staticmethod
    def cleanup_sandbox(sandbox_path: str) -> bool:
        if os.path.exists(sandbox_path):
            shutil.rmtree(sandbox_path, ignore_errors=True)
            return True
        return False
