from app.core.llm_gateway import LLMGateway

def test_prompt_registry():
    gateway = LLMGateway()
    prompt = gateway.get_prompt("analyzer", input="Refactor database schema")
    assert "Refactor database schema" in prompt

def test_mock_completion():
    gateway = LLMGateway()
    res = gateway.mock_completion("coder", input="Create a new endpoint")
    assert res["status"] == "success"
    assert res["model"] == "gpt-4o"
    assert "Create a new endpoint" in res["prompt_used"]
    assert "coder" in res["response"]
