from app.core.daemon_runner import NoxiaiDaemonRunner

def test_daemon_runner():
    daemon = NoxiaiDaemonRunner()
    pulse = daemon.start_autonomous_pulse()

    assert pulse["daemon_status"] == "active"
    assert pulse["pipeline_result"]["status"] == "executed_successfully"
    assert pulse["evolution_result"]["integrated_status"] == "success"
