class IntentTransmuter:
    def __init__(self):
        self.transmutation_rules = {
            "durum": {"action": "fetch_telemetry_snapshot", "target": "system"},
            "temizle": {"action": "optimize_memory_cache", "target": "memory"},
            "güvenlik": {"action": "inspect_firewall_logs", "target": "security"}
        }

    def transmute(self, user_command: str) -> dict:
        cmd_lower = user_command.lower().strip()
        matched_rule = None

        for keyword, rule in self.transmutation_rules.items():
            if keyword in cmd_lower:
                matched_rule = rule
                break

        if not matched_rule:
            matched_rule = {"action": "execute_standard_dialogue", "target": "dialogue_engine"}

        return {
            "raw_command": user_command,
            "transmuted_action": matched_rule["action"],
            "target_subsystem": matched_rule["target"],
            "status": "transmuted_successfully"
        }
