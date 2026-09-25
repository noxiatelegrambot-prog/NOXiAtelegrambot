import subprocess
import os

class GitTool:
    @staticmethod
    def run_git_command(args: list[str]) -> dict:
        try:
            result = subprocess.run(
                ["git"] + args,
                capture_output=True,
                text=True,
                check=True
            )
            return {"success": True, "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"success": False, "output": e.stderr}

    @classmethod
    def create_feature_branch(cls, branch_name: str) -> dict:
        cls.run_git_command(["checkout", "-b", branch_name])
        return {"success": True, "branch": branch_name}

    @classmethod
    def commit_changes(cls, message: str) -> dict:
        cls.run_git_command(["add", "."])
        result = cls.run_git_command(["commit", "-m", message])
        return result
