class GitHubIntegrationManager:
    def __init__(self, repo_name: str, token: str = "mock-token"):
        self.repo_name = repo_name
        self.token = token
        self.branches = ["main"]
        self.pull_requests = []

    def create_branch(self, branch_name: str) -> bool:
        if branch_name in self.branches:
            return False
        self.branches.append(branch_name)
        return True

    def create_pull_request(self, title: str, head_branch: str, base_branch: str = "main") -> dict:
        pr_item = {
            "id": len(self.pull_requests) + 1,
            "title": title,
            "head": head_branch,
            "base": base_branch,
            "status": "open"
        }
        self.pull_requests.append(pr_item)
        return pr_item
