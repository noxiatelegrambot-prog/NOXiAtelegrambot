from app.core.swarm_coordinator import SwarmCoordinator

def test_swarm_coordinator_consensus():
    coordinator = SwarmCoordinator()
    
    # All 4 agents active -> Consensus should be True
    res = coordinator.evaluate_swarm_consensus("System Boot")
    assert res["consensus"] is True
    assert res["action"] == "execute_synchronized_operation"

    # Disable two agents -> Active count drops to 2 (< 3) -> Consensus False
    coordinator.toggle_agent("security_agent", False)
    coordinator.toggle_agent("memory_agent", False)
    
    res_degraded = coordinator.evaluate_swarm_consensus("High Security Alert")
    assert res_degraded["consensus"] is False
    assert res_degraded["action"] == "halt_operations"
