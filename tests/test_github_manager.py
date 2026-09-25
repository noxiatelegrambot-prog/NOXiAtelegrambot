from app.core.github_manager import GitHubManager

def test_commit_message_formatting():
    msg = GitHubManager.format_commit_message("feat", "sandbox", "add isolation layer", "1-15")
    assert msg == "feat(sandbox): add isolation layer (Faz 2 - Items 1-15)"

def test_repository_sync_validation():
    res_ready = GitHubManager.validate_repository_sync_status(True, True)
    assert res_ready["sync_ready"] is True

    res_not_ready = GitHubManager.validate_repository_sync_status(False, True)
    assert res_not_ready["sync_ready"] is False
