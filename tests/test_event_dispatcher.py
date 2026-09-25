from app.core.event_dispatcher import EventNotificationDispatcher

def test_event_notification_dispatcher():
    dispatcher = EventNotificationDispatcher()
    received_events = []

    def mock_listener(data):
        received_events.append(data)

    dispatcher.subscribe("security_alert", mock_listener)
    
    count = dispatcher.dispatch("security_alert", {"level": "high", "msg": "Unauthorized attempt"})
    assert count == 1
    assert len(received_events) == 1
    assert received_events[0]["level"] == "high"
    assert len(dispatcher.event_log) == 1
