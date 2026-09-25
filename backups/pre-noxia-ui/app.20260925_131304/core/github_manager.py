class GitHubManager:
    @staticmethod
    def format_commit_message(change_type: str, scope: str, description: str, item_range: str) -> str:
        # Follow conventional commits standard used across the project
        return f"{change_type}({scope}): {description} (Faz 2 - Items {item_range})"

    @staticmethod
    def validate_repository_sync_status(is_clean: bool, has_remote: bool) -> dict:
        sync_ready = is_clean and has_remote
        return {
            "status": "success",
            "sync_ready": sync_ready,
            "message": "Repository is synchronized and ready for deployment." if sync_ready else "Uncommitted changes or missing remote configuration."
        }
