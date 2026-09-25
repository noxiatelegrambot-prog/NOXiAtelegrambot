from app.core.tester_agent import TesterAgent

def test_tester_agent():
    res = TesterAgent.run_tests_and_report("app.core.sandbox_agent")
    assert res["status"] == "success"
    assert res["failed_tests"] == 0

    fail_res = TesterAgent.run_tests_and_report("broken_module")
    assert fail_res["status"] == "failed"
    assert fail_res["failed_tests"] == 1
