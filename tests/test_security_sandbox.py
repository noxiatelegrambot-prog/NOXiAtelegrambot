from app.core.security_sandbox import RateLimiter, SecuritySandbox

def test_rate_limiter():
    limiter = RateLimiter(max_requests=2, window_seconds=10)
    user_id = 999
    
    assert limiter.is_allowed(user_id) is True
    assert limiter.is_allowed(user_id) is True
    assert limiter.is_allowed(user_id) is False # Exceeded limit

def test_security_sandbox_code_filtering():
    sandbox = SecuritySandbox()
    safe_code = "def add(a, b): return a + b"
    unsafe_code = "import os; os.system('rm -rf /')"

    assert sandbox.validate_safe_code(safe_code) is True
    assert sandbox.validate_safe_code(unsafe_code) is False
