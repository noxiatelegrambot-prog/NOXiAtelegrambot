class DynamicStateSyncEngine:
    def __init__(self):
        self.config_store = {
            "max_cache_size": 5,
            "security_strictness": "high",
            "autonomous_mode": True,
            "health_threshold": 70.0
        }

    def update_config(self, key: str, value) -> dict:
        if key not in self.config_store:
            return {"status": "error", "reason": "unknown_config_key"}
        
        self.config_store[key] = value
        return {
            "status": "synchronized",
            "key": key,
            "new_value": value
        }

    def get_config(self, key: str):
        return self.config_store.get(key)
