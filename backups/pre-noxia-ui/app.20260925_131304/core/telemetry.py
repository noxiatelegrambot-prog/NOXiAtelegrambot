import time

class TelemetryEngine:
    def __init__(self):
        self.metrics = []
        self.start_time = time.time()

    def record_metric(self, name: str, value: float, unit: str = "ms"):
        metric_item = {
            "name": name,
            "value": value,
            "unit": unit,
            "timestamp": time.time()
        }
        self.metrics.append(metric_item)
        return metric_item

    def get_uptime(self) -> float:
        return time.time() - self.start_time

    def get_summary(self) -> dict:
        return {
            "uptime_seconds": round(self.get_uptime(), 2),
            "total_metrics_recorded": len(self.metrics),
            "recent_metrics": self.metrics[-5:]
        }
