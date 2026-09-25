from app.core.event_bus import EventBus

def test_event_bus_pub_sub():
    bus = EventBus()
    events_received = []

    def mock_listener(data):
        events_received.append(data)
        return "processed"

    bus.subscribe("task_created", mock_listener)
    
    res = bus.publish("task_created", {"task_id": "123", "title": "Test Event"})
    assert res["status"] == "success"
    assert res["dispatched_to_count"] == 1
    assert len(events_received) == 1
    assert events_received[0]["task_id"] == "123"
