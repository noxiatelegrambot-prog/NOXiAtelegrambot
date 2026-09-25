from app.core.test_agent import TestAgent
from app.core.sandbox_manager import SandboxManager
from app.core.developer_agent import DeveloperAgent

def test_test_agent_execution():
    sb = SandboxManager.create_sandbox("test_agent_task")
    path = sb["sandbox_path"]
    
    # Write a simple passing test file
    test_code = "def test_math():\n    assert 1 + 1 == 2\n"
    DeveloperAgent.write_code_to_sandbox(path, "test_sample.py", test_code)
    
    res = TestAgent.run_tests_in_sandbox(path)
    assert res["status"] == "success"
    assert res["tests_passed"] is True
    
    SandboxManager.cleanup_sandbox(path)
