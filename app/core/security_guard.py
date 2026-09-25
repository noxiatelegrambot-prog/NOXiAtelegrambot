import re

class SecurityGuard:
    @staticmethod
    def mask_secrets(text: str) -> str:
        # Redact potential API keys or tokens
        masked = re.sub(r'(sk-[a-zA-Z0-9]{20,})', 'sk-***REDACTED***', text)
        masked = re.sub(r'(\d{8,10}:[a-zA-Z0-9_-]{35})', 'tg-token-***REDACTED***', masked)
        return masked

    @staticmethod
    def verify_rbac(user_role: str, required_role: str) -> bool:
        roles_hierarchy = {"user": 1, "moderator": 2, "admin": 3}
        user_level = roles_hierarchy.get(user_role, 0)
        required_level = roles_hierarchy.get(required_role, 99)
        return user_level >= required_level
