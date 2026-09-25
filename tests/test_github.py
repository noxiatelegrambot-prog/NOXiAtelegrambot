from app.core.github_integration import GitHubIntegrationManager

def test_github_manager_branch_and_pr():
    gh = GitHubIntegrationManager("selenaysasmaz62-afk/telegram-bot")
    
    assert gh.create_branch("feature/noxia-auto-patch") is True
    assert gh.create_branch("feature/noxia-auto-patch") is False # duplicate check

    pr = gh.create_pull_request("feat: autonomous AST patch", "feature/noxia-auto-patch")
    assert pr["status"] == "open"
    assert pr["head"] == "feature/noxia-auto-patch"
    assert len(gh.pull_requests) == 1
