
import time
import logging

class AIRouterError(Exception):
    pass

class ProviderHealth:
    def __init__(self, name: str, cooldown_seconds: int = 60):
        self.name = name
        self.available = True
        self.failures = 0
        self.cooldown_seconds = cooldown_seconds
        self.last_failure_time = 0.0

    def record_failure(self):
        self.failures += 1
        self.available = False
        self.last_failure_time = time.time()

    def record_success(self):
        self.failures = 0
        self.available = True
        self.last_failure_time = 0.0

    def check_cooldown(self) -> bool:
        if not self.available and self.last_failure_time > 0:
            if time.time() - self.last_failure_time >= self.cooldown_seconds:
                self.available = True
                self.failures = 0
                return True
        return self.available
