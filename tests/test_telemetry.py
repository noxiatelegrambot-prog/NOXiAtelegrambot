from app.core.telemetry_analyzer import DeepTelemetryAnalyzer

def test_deep_telemetry_analyzer():
    analyzer = DeepTelemetryAnalyzer()

    # Collect snapshot with zero errors (Stable)
    snap = analyzer.collect_snapshot(active_modules_count=34, error_count=0)
    assert snap["status"] == "stable"
    assert analyzer.get_system_health_score() == 100.0

    # Collect snapshot with errors (Degraded)
    snap_err = analyzer.collect_snapshot(active_modules_count=34, error_count=2)
    assert snap_err["status"] == "degraded"
    assert analyzer.get_system_health_score() == 70.0
