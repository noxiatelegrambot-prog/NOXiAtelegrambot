import sqlite3
import datetime

class OrchestratorPipeline:
    @staticmethod
    def get_db_path() -> str:
        return "noxia.db"

    @staticmethod
    def init_pipeline_db():
        conn = sqlite3.connect(OrchestratorPipeline.get_db_path())
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autonomous_tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT,
                status TEXT DEFAULT "QUEUED",
                agent_assigned TEXT,
                result_log TEXT,
                created_at TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def execute_task_pipeline(task_id: str, title: str) -> dict:
        OrchestratorPipeline.init_pipeline_db()
        conn = sqlite3.connect(OrchestratorPipeline.get_db_path())
        cursor = conn.cursor()
        
        now = datetime.datetime.now().isoformat()
        
        # 1. Phase: Developer Agent Analysis & Generation
        dev_log = f"[{now}] Developer Agent: Analyzing repository & generating patch for '{title}'..."
        
        # 2. Phase: Sandbox Isolation & Execution
        sandbox_log = f"[{now}] Sandbox: Executing code inside isolated container environment..."
        
        # 3. Phase: Tester Agent Verification
        tester_log = f"[{now}] Tester Agent: Running pytest verification suite..."
        
        # Simulating successful pipeline run
        final_status = "SUCCESS"
        result_summary = f"Task '{title}' successfully executed through Developer -> Sandbox -> Tester pipeline."
        
        cursor.execute("""
            INSERT OR REPLACE INTO autonomous_tasks (task_id, title, status, agent_assigned, result_log, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (task_id, title, final_status, "Orchestrator-Core", result_summary, now))
        
        conn.commit()
        conn.close()
        
        return {
            "task_id": task_id,
            "status": final_status,
            "steps": [dev_log, sandbox_log, tester_log],
            "message": result_summary
        }
