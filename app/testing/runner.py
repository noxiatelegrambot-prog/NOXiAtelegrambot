import subprocess
import sys
from pathlib import Path


class TestRunner:
    def compile(self, project_root: Path) -> tuple[bool, str]:
        result = subprocess.run(
            [sys.executable, "-m", "compileall", "-q", "app"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=120,
        )

        output = (result.stdout + result.stderr).strip()

        return result.returncode == 0, output

    def pytest(self, project_root: Path) -> tuple[bool, str]:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=300,
        )

        output = (result.stdout + result.stderr).strip()

        return result.returncode == 0, output
