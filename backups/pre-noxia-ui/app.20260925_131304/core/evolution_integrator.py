from app.core.self_evolution import AutonomousSelfEvolutionEngine

class EvolutionIntegrator:
    def __init__(self):
        self.engine = AutonomousSelfEvolutionEngine()

    def run_pipeline_evolution(self) -> dict:
        cycle = self.engine.execute_evolution_cycle()
        return {
            "integrated_status": "success",
            "evolution_details": cycle
        }
