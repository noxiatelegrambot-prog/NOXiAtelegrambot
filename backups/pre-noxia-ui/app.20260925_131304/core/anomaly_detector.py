class AutonomousAnomalyDetector:
    def __init__(self, deviation_threshold: float = 3.0):
        self.deviation_threshold = deviation_threshold
        self.metric_history = []

    def evaluate_metric(self, metric_value: float) -> dict:
        self.metric_history.append(metric_value)
        is_anomaly = False
        
        if len(self.metric_history) > 3:
            baseline = sum(self.metric_history[:-1]) / len(self.metric_history[:-1])
            difference = abs(metric_value - baseline)
            if difference > self.deviation_threshold * (abs(baseline) + 1.0):
                is_anomaly = True

        return {
            "metric": metric_value,
            "is_anomaly": is_anomaly,
            "action": "trigger_mitigation_protocol" if is_anomaly else "normal_operation"
        }
