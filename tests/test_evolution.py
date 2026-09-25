from app.core.self_evolution import AutonomousSelfEvolutionEngine

def test_autonomous_self_evolution():
    engine = AutonomousSelfEvolutionEngine()
    
    proposal = engine.scan_and_propose_evolution()
    assert proposal["status"] == "proposal_generated"

    cycle = engine.execute_evolution_cycle()
    assert cycle["evolution_status"] in ["committed_successfully", "rolled_back"]
    assert "proposal" in cycle
