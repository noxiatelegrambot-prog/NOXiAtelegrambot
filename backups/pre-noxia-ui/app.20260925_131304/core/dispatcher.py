
class TelegramDispatcher:
    def __init__(self, allowed_user_ids=None):
        self.allowed_user_ids = allowed_user_ids or []
        self.routes = {}

    def register_handler(self, command: str, func):
        self.routes[command] = func

    def authenticate_user(self, user_id: int) -> bool:
        if not self.allowed_user_ids:
            return True # Open mode if no whitelist set
        return user_id in self.allowed_user_ids

    def dispatch(self, user_id: int, command: str, payload: dict = None) -> dict:
        if not self.authenticate_user(user_id):
            return {"status": "unauthorized", "response": "Access denied."}
        
        handler = self.routes.get(command)
        if not handler:
            return {"status": "not_found", "response": f"Unknown command: {command}"}
        
        try:
            res = handler(payload or {})
            return {"status": "success", "response": res}
        except Exception as e:
            return {"status": "error", "response": str(e)}
