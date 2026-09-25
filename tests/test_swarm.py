
from app.core.swarm import SwarmCoordinator

def test_swarm_coordination_and_blackboard():
    coordinator = SwarmCoordinator()
    coordinator.register_agent("Researcher")
    coordinator.register_agent("Developer")
    
    result = coordinator.coordinate_task("Refactor dispatcher module")
    
    assert result["status"] == "coordinated"
    assert result["registered_agents"] == 2
    assert coordinator.blackboard.read("current_task") == "Refactor dispatcher module"
    
    feed = coordinator.blackboard.get_feed()
    assert len(feed) == 1
    assert feed[0]["sender"] == "Coordinator"
