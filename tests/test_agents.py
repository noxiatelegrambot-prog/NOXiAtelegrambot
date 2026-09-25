
from app.core.agents import ResearcherAgent, DeveloperAgent

def test_researcher_agent_execution():
    agent = ResearcherAgent()
    assert agent.name == "Researcher"
    assert agent.status == "idle"
    
    res = agent.execute({"query": "Telegram bot API"})
    assert res["status"] == "success"
    assert "Telegram bot API" in res["findings"]

def test_developer_agent_execution():
    agent = DeveloperAgent()
    assert agent.role == "code_generation"
    
    res = agent.execute({"spec": "add handler"})
    assert res["status"] == "success"
    assert "add handler" in res["code"]
