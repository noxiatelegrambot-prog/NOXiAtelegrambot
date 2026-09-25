import re

class AutonomousFirewall:
    def __init__(self):
        self.blocked_patterns = [
            r"union\s+select",
            r"<script>",
            r"drop\s+table",
            r"exec\s*\(",
            r"system\s*\("
        ]
        self.security_logs = []

    def inspect_payload(self, user_id: int, payload: str) -> dict:
        payload_lower = payload.lower()
        is_safe = True
        matched_threat = None

        for pattern in self.blocked_patterns:
            if re.search(pattern, payload_lower):
                is_safe = False
                matched_threat = pattern
                break

        inspection_result = {
            "user_id": user_id,
            "payload": payload,
            "is_safe": is_safe,
            "threat": matched_threat,
            "action": "allow" if is_safe else "block_and_flag"
        }
        
        self.security_logs.append(inspection_result)
        return inspection_result
