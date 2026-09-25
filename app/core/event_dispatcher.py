class EventNotificationDispatcher:
    def __init__(self):
        self.subscribers = {}
        self.event_log = []

    def subscribe(self, event_type: str, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def dispatch(self, event_type: str, data: dict) -> int:
        event_record = {
            "type": event_type,
            "data": data,
            "status": "dispatched"
        }
        self.event_log.append(event_record)
        
        notified_count = 0
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                try:
                    callback(data)
                    notified_count += 1
                except Exception:
                    pass
        return notified_count
