from dataclasses import dataclass
from pathlib import Path
import subprocess


@dataclass
class ChangeResult:
    success: bool
    message: str
    branch: str


def apply_patch(patch_file: str, branch: str = "noxia-agent") -> ChangeResult:
    subprocess.run(
        ["git", "checkout", "-b", branch],
        check=False,
        capture_output=True,
        text=True,
    )

    result = subprocess.run(
        ["git", "apply", "--check", patch_file],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return ChangeResult(False, result.stderr.strip(), branch)

    result = subprocess.run(
        ["git", "apply", patch_file],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return ChangeResult(False, result.stderr.strip(), branch)

    return ChangeResult(True, "Patch applied successfully.", branch)
