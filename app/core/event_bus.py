class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type: str, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def publish(self, event_type: str, data: dict) -> dict:
        results = []
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                res = callback(data)
                results.append(res)
        return {
            "status": "success",
            "event_type": event_type,
            "dispatched_to_count": len(results),
            "results": results
        }
