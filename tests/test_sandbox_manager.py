from app.core.sandbox_manager import SandboxManager

def test_sandbox_lifecycle():
    task_id = "task_test_123"
    sb = SandboxManager.create_sandbox(task_id)
    assert sb["status"] == "success"
    assert "sandbox_path" in sb

    path = sb["sandbox_path"]
    res = SandboxManager.execute_command_in_sandbox(path, ["python3", "-c", "print('Hello Sandbox')"])
    assert res["status"] == "success"
    assert "Hello Sandbox" in res["stdout"]

    cleanup = SandboxManager.cleanup_sandbox(path)
    assert cleanup is True

def test_sandbox_security_denylist():
    path = "/tmp/dummy_sandbox"
    res = SandboxManager.execute_command_in_sandbox(path, ["rm", "-rf", "/"])
    assert res["status"] == "blocked"
