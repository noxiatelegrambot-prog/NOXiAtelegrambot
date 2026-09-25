from app.core.research_agent import ResearchAgent

def test_research_synthesis():
    res = ResearchAgent.synthesize_research("Python async best practices")
    assert res["status"] == "success"
    assert res["sources_count"] == 2
    assert "Python async best practices" in res["query"]
    assert "Synthesized research findings" in res["summary"]
