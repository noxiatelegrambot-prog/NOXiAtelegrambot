import re

class SecurityGuard:
    @staticmethod
    def redact_sensitive_data(text: str) -> str:
        # Mask OpenAI keys and Telegram bot tokens in logs/text
        redacted = re.sub(r'(sk-[a-zA-Z0-9]{20,})', '***REDACTED_API_KEY***', text)
        redacted = re.sub(r'(\d{9,10}:[a-zA-Z0-9_-]{35})', '***REDACTED_BOT_TOKEN***', redacted)
        return redacted

    @staticmethod
    def authorize_admin(user_id: int, admin_whitelist: list) -> bool:
        return user_id in admin_whitelist
