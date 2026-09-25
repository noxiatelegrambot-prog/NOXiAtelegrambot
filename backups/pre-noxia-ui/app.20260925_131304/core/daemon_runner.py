from app.core.master_orchestrator import MasterOrchestrationCore
from app.core.evolution_integrator import EvolutionIntegrator

class NoxiaiDaemonRunner:
    def __init__(self):
        self.orchestrator = MasterOrchestrationCore()
        self.evolution = EvolutionIntegrator()
        self.is_running = False

    def start_autonomous_pulse(self) -> dict:
        self.is_running = True
        
        # Execute one complete autonomous ecosystem pulse
        pipeline_res = self.orchestrator.process_global_pipeline(0, "system_autonomous_pulse")
        evolution_res = self.evolution.run_pipeline_evolution()

        return {
            "daemon_status": "active",
            "pipeline_result": pipeline_res,
            "evolution_result": evolution_res
        }
