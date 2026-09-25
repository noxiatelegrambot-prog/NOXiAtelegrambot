from app.core.intent_transmuter import IntentTransmuter

def test_intent_transmuter():
    transmuter = IntentTransmuter()

    # Test telemetry rule translation
    res1 = transmuter.transmute("Sistem durumunu göster")
    assert res1["transmuted_action"] == "fetch_telemetry_snapshot"
    assert res1["target_subsystem"] == "system"

    # Test memory cleanup rule translation
    res2 = transmuter.transmute("Lütfen önbelleği temizle")
    assert res2["transmuted_action"] == "optimize_memory_cache"
    assert res2["target_subsystem"] == "memory"
    assert res2["status"] == "transmuted_successfully"
