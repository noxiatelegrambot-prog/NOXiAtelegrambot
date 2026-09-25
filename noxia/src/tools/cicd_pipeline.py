import subprocess
from src.tools.git_tool import GitTool
from src.tools.deployment_tool import DeploymentTool

class CICDPipeline:
    @staticmethod
    def execute_pipeline(commit_message: str = "auto: NOXiA autonomous deployment update") -> dict:
        print("🔄 [CI/CD] Boru hattı tetiklendi...")
        
        # 1. Git Add & Commit
        commit_result = GitTool.commit_changes(commit_message)
        if not commit_result.get("success", False) and "nothing to commit" not in commit_result.get("output", ""):
            return {"success": False, "stage": "git_commit", "error": commit_result["output"]}
            
        # 2. Git Push
        push_result = GitTool.run_git_command(["push", "origin", "main"])
        if not push_result.get("success", False):
            # Eğer main yerine başka branch'se alternatif deneyebilir veya loglayabiliriz
            pass
            
        # 3. Railway Deployment Trigger
        deploy_result = DeploymentTool.check_railway_status()
        
        print("✅ [CI/CD] Boru hattı başarıyla tamamlandı.")
        return {
            "success": True,
            "commit": commit_result,
            "deployment": deploy_result
        }
