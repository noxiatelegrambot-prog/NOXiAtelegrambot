from dataclasses import dataclass
import subprocess


@dataclass
class ChangeResult:
    success: bool
    message: str
    branch: str


def run_git(*args):
    return subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
    )


def create_agent_branch(
    branch: str = "noxia-developer",
    base: str = "noxia-v1",
) -> ChangeResult:
    current = run_git("branch", "--show-current").stdout.strip()

    if current != base:
        result = run_git("checkout", base)
        if result.returncode != 0:
            return ChangeResult(False, result.stderr.strip(), branch)

    result = run_git("pull", "--ff-only", "origin", base)
    if result.returncode != 0:
        return ChangeResult(False, result.stderr.strip(), branch)

    existing = run_git("branch", "--list", branch)

    if existing.stdout.strip():
        result = run_git("checkout", branch)
    else:
        result = run_git("checkout", "-b", branch)

    if result.returncode != 0:
        return ChangeResult(False, result.stderr.strip(), branch)

    return ChangeResult(
        True,
        f"Developer branch ready: {branch}",
        branch,
    )


def validate_patch(patch_file: str) -> ChangeResult:
    branch = run_git("branch", "--show-current").stdout.strip()

    result = run_git("apply", "--check", patch_file)

    if result.returncode != 0:
        return ChangeResult(
            False,
            result.stderr.strip(),
            branch,
        )

    return ChangeResult(
        True,
        "Patch validation passed.",
        branch,
    )


def apply_patch(
    patch_file: str,
    commit_message: str,
) -> ChangeResult:
    branch = run_git("branch", "--show-current").stdout.strip()

    if branch == "noxia-v1":
        return ChangeResult(
            False,
            "Protected branch: noxia-v1",
            branch,
        )

    check = validate_patch(patch_file)

    if not check.success:
        return check

    result = run_git("apply", patch_file)

    if result.returncode != 0:
        return ChangeResult(
            False,
            result.stderr.strip(),
            branch,
        )

    result = run_git("add", "-A")

    if result.returncode != 0:
        return ChangeResult(False, result.stderr.strip(), branch)

    result = run_git("commit", "-m", commit_message)

    if result.returncode != 0:
        return ChangeResult(False, result.stderr.strip(), branch)

    return ChangeResult(
        True,
        "Controlled change committed.",
        branch,
    )
