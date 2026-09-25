import time

class RateLimiter:
    def __init__(self, max_requests: int = 5, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}

    def is_allowed(self, user_id: int) -> bool:
        now = time.time()
        user_history = self.requests.get(user_id, [])
        
        # Filter timestamps within the window
        user_history = [t for t in user_history if now - t < self.window_seconds]
        
        if len(user_history) >= self.max_requests:
            self.requests[user_id] = user_history
            return False
            
        user_history.append(now)
        self.requests[user_id] = user_history
        return True

class SecuritySandbox:
    def __init__(self):
        self.forbidden_keywords = ["__import__", "eval", "exec", "os.system", "subprocess"]

    def validate_safe_code(self, code_str: str) -> bool:
        for keyword in self.forbidden_keywords:
            if keyword in code_str:
                return False
        return True
