
class SelfDevelopmentManager:
    def __init__(self):
        self.patch_history = []

    def propose_patch(self, target_file: str, patch_content: str, reason: str) -> dict:
        if not target_file or not patch_content:
            raise ValueError("Target file and patch content are required.")
        
        patch_record = {
            "id": len(self.patch_history) + 1,
            "target_file": target_file,
            "patch_content": patch_content,
            "reason": reason,
            "status": "proposed"
        }
        self.patch_history.append(patch_record)
        return patch_record

    def apply_patch(self, patch_id: int) -> bool:
        for p in self.patch_history:
            if p["id"] == patch_id:
                p["status"] = "applied"
                return True
        return False
