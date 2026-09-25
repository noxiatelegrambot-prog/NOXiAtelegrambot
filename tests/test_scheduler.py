from app.core.task_scheduler import AutonomousTaskScheduler

def test_autonomous_scheduler():
    scheduler = AutonomousTaskScheduler()
    executed_flag = []

    def dummy_task():
        executed_flag.append(True)

    scheduler.register_task("health_check_cron", 10, dummy_task)

    # Tick at t = 5 (should not trigger yet because interval is 10)
    triggered_1 = scheduler.tick(5.0)
    assert len(triggered_1) == 0
    assert len(executed_flag) == 0

    # Tick at t = 12 (should trigger)
    triggered_2 = scheduler.tick(12.0)
    assert "health_check_cron" in triggered_2
    assert len(executed_flag) == 1
