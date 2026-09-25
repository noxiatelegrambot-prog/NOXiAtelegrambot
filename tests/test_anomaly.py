from app.core.anomaly_detector import AutonomousAnomalyDetector

def test_autonomous_anomaly_detector():
    detector = AutonomousAnomalyDetector(deviation_threshold=2.0)

    # Establish baseline
    detector.evaluate_metric(10.0)
    detector.evaluate_metric(11.0)
    detector.evaluate_metric(10.5)

    # Normal metric value
    res_normal = detector.evaluate_metric(10.2)
    assert res_normal["is_anomaly"] is False
    assert res_normal["action"] == "normal_operation"

    # Extreme anomaly metric value
    res_anomaly = detector.evaluate_metric(95.0)
    assert res_anomaly["is_anomaly"] is True
    assert res_anomaly["action"] == "trigger_mitigation_protocol"
