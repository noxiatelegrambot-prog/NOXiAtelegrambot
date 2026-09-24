from pathlib import Path
import shutil
import tempfile


class Sandbox:
    def __init__(self, project_root: Path):
        self.project_root = project_root.resolve()

    def create(self) -> Path:
        sandbox = Path(
            tempfile.mkdtemp(prefix="noxia-sandbox-")
        )

        for item in self.project_root.iterdir():
            if item.name in {
                ".git",
                "__pycache__",
                ".pytest_cache",
                "data",
            }:
                continue

            destination = sandbox / item.name

            if item.is_dir():
                shutil.copytree(item, destination)
            else:
                shutil.copy2(item, destination)

        return sandbox

    def cleanup(self, sandbox: Path) -> None:
        if sandbox.exists():
            shutil.rmtree(sandbox, ignore_errors=True)
