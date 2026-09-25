from app.core.research_agent import ResearchAgent

def test_research_agent():
    res = ResearchAgent.conduct_research("Python async generators")
    assert res["status"] == "success"
    assert len(res["sources"]) == 2
    assert "Synthesized" in res["synthesis"]
