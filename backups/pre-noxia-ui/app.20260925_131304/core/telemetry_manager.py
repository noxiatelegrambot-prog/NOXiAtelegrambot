import time

class TelemetryManager:
    def __init__(self):
        self.metrics = []

    def record_metric(self, metric_name: str, value: float) -> dict:
        entry = {
            "timestamp": time.time(),
            "metric_name": metric_name,
            "value": value
        }
        self.metrics.append(entry)
        return {
            "status": "success",
            "recorded": entry,
            "total_metrics_count": len(self.metrics)
        }

    def get_summary(self) -> dict:
        return {
            "status": "success",
            "count": len(self.metrics),
            "metrics": self.metrics
        }
