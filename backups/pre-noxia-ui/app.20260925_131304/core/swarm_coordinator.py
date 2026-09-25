class SwarmCoordinator:
    def __init__(self):
        self.agents = {
            "dialogue_agent": True,
            "security_agent": True,
            "memory_agent": True,
            "error_agent": True
        }
        self.consensus_log = []

    def evaluate_swarm_consensus(self, event_context: str) -> dict:
        active_agents = [name for name, status in self.agents.items() if status]
        consensus_reached = len(active_agents) >= 3
        
        decision = {
            "context": event_context,
            "active_agents_count": len(active_agents),
            "consensus": consensus_reached,
            "action": "execute_synchronized_operation" if consensus_reached else "halt_operations"
        }
        self.consensus_log.append(decision)
        return decision

    def toggle_agent(self, agent_name: str, status: bool):
        if agent_name in self.agents:
            self.agents[agent_name] = status
