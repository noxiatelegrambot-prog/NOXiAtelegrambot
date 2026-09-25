
import pytest
from app.ai.planner import TaskPlanner, PlannerError

def test_planner_analysis_and_agents():
    planner = TaskPlanner()
    plan = planner.analyze_and_plan("Python kodu yaz ve test et")
    
    assert "developer" in plan["agents"]
    assert "tester" in plan["agents"]
    assert plan["requires_review"] is True
    assert planner.validate_plan(plan) is True

def test_planner_invalid_prompt():
    planner = TaskPlanner()
    with pytest.raises(PlannerError):
        planner.analyze_and_plan("")
