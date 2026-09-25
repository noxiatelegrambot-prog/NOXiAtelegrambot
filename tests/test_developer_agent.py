from app.core.developer_agent import DeveloperAgent
from app.core.sandbox_manager import SandboxManager

def test_developer_code_writing():
    sb = SandboxManager.create_sandbox("dev_task_01")
    path = sb["sandbox_path"]
    
    code = DeveloperAgent.generate_module_scaffold("calculator")
    res = DeveloperAgent.write_code_to_sandbox(path, "calculator.py", code)
    
    assert res["status"] == "success"
    assert "calculator.py" in res["file_path"]
    
    # Clean up
    SandboxManager.cleanup_sandbox(path)

def test_module_scaffold_generation():
    scaffold = DeveloperAgent.generate_module_scaffold("auth")
    assert "class Auth" in scaffold
    assert "self.name = \"auth\"" in scaffold
