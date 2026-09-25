from app.core.telemetry_manager import TelemetryManager

def test_telemetry_recording():
    tm = TelemetryManager()
    res = tm.record_metric("execution_time_ms", 145.2)
    assert res["status"] == "success"
    assert res["recorded"]["metric_name"] == "execution_time_ms"
    assert res["recorded"]["value"] == 145.2

    summary = tm.get_summary()
    assert summary["count"] == 1
