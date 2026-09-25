from app.core.security_guard import SecurityGuard

def test_security_guard_redaction():
    sample_log = "Error connecting with token 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ123456789 and key sk-proj-1234567890abcdef"
    cleaned = SecurityGuard.redact_sensitive_data(sample_log)
    
    assert "123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ123456789" not in cleaned
    assert "sk-proj-1234567890abcdef" not in cleaned
    assert "***REDACTED_BOT_TOKEN***" in cleaned
    assert "***REDACTED_API_KEY***" in cleaned

def test_admin_authorization():
    admins = [1001, 1002]
    assert SecurityGuard.authorize_admin(1001, admins) is True
    assert SecurityGuard.authorize_admin(9999, admins) is False
