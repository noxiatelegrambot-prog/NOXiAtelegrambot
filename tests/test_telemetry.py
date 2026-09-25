from app.core.telemetry import TelemetryEngine

def test_telemetry_engine_metrics():
    telemetry = TelemetryEngine()
    metric = telemetry.record_metric("response_time", 45.2, "ms")
    
    assert metric["name"] == "response_time"
    assert metric["value"] == 45.2
    assert telemetry.get_uptime() >= 0.0

    summary = telemetry.get_summary()
    assert summary["total_metrics_recorded"] == 1
    assert len(summary["recent_metrics"]) == 1
