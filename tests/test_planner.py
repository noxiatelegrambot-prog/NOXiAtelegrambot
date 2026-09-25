from app.core.planner_agent import AutonomousPlanner

def test_autonomous_planner():
    plan = AutonomousPlanner.create_execution_plan("Build a telegram plugin")
    assert plan["status"] == "success"
    assert len(plan["plan"]) == 3
    assert plan["plan"][1]["depends_on"] == ["sub_1"]
