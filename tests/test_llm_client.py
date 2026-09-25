from app.core.llm_client import LLMClient

def test_llm_client_initialization():
    client = LLMClient("gpt-4o-mini")
    validation = client.validate_client()
    assert validation["status"] == "ready"
    assert validation["model"] == "gpt-4o-mini"

def test_llm_simulation():
    client = LLMClient()
    res = client.simulate_inference("Hello NOXiA")
    assert res["status"] == "success"
    assert "usage" in res
    assert res["usage"]["total_tokens"] == 40
