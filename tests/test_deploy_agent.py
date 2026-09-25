from app.core.deploy_agent import DeployAgent

def test_railway_deploy():
    res = DeployAgent.trigger_railway_deploy("git_commit_abc1234")
    assert res["status"] == "success"
    assert res["health_status"] == "healthy"

    fail_res = DeployAgent.trigger_railway_deploy("")
    assert fail_res["status"] == "failed"
    assert "Missing commit hash" in fail_res["error"]
