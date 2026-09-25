import time

class DeepTelemetryAnalyzer:
    def __init__(self):
        self.metrics_history = []

    def collect_snapshot(self, active_modules_count: int, error_count: int) -> dict:
        snapshot = {
            "timestamp": time.time(),
            "active_modules": active_modules_count,
            "error_rate": error_count,
            "status": "stable" if error_count == 0 else "degraded"
        }
        self.metrics_history.append(snapshot)
        return snapshot

    def get_system_health_score(self) -> float:
        if not self.metrics_history:
            return 100.0
        
        last = self.metrics_history[-1]
        errors = last["error_rate"]
        
        # Calculate health percentage based on error count
        score = max(0.0, 100.0 - (errors * 15.0))
        return round(score, 2)
