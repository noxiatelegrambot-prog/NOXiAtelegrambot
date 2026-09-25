from app.core.developer_starter import DeveloperStarter

def test_developer_project_analysis():
    res = DeveloperStarter.analyze_project_structure()
    assert res["status"] == "success"
    assert res["code_generation_ready"] is True

def test_faz1_full_system_smoke_test():
    res = DeveloperStarter.run_faz1_smoke_test()
    assert res["status"] == "success"
    assert res["faz_1_completed"] is True
    assert res["total_subsystems"] == 11
    assert "SystemCore" in res["subsystems"]
    assert "Orchestrator" in res["subsystems"]
