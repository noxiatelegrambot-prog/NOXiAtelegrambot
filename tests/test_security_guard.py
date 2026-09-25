from app.core.security_guard import SecurityGuard

def test_secret_masking():
    secret_text = "My OpenAI key is sk-1234567890abcdefghijklmnopqrstuv and bot token is 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ_12345678"
    safe_text = SecurityGuard.mask_secrets(secret_text)
    assert "sk-***REDACTED***" in safe_text
    assert "tg-token-***REDACTED***" in safe_text
    assert "sk-1234567890abcdefghijklmnopqrstuv" not in safe_text

def test_rbac_authorization():
    assert SecurityGuard.verify_rbac("admin", "moderator") is True
    assert SecurityGuard.verify_rbac("user", "admin") is False
    assert SecurityGuard.verify_rbac("moderator", "moderator") is True
