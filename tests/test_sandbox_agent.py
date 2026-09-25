from app.core.sandbox_agent import SandboxAgent

def test_sandbox_execution():
    res = SandboxAgent.execute_in_sandbox("print('Hello Sandbox')")
    assert res["status"] == "success"
    assert res["exit_code"] == 0

    error_res = SandboxAgent.execute_in_sandbox("syntax_error_code")
    assert error_res["status"] == "error"
    assert error_res["error_type"] == "SyntaxError"
