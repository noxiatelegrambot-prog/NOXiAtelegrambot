from app.core.evolution_integrator import EvolutionIntegrator

def test_evolution_integrator():
    integrator = EvolutionIntegrator()
    result = integrator.run_pipeline_evolution()
    
    assert result["integrated_status"] == "success"
    assert "evolution_details" in result
    assert result["evolution_details"]["evolution_status"] in ["committed_successfully", "rolled_back"]
