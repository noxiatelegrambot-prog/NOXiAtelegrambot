from app.core.state_sync import DynamicStateSyncEngine

def test_dynamic_state_sync():
    sync_engine = DynamicStateSyncEngine()

    assert sync_engine.get_config("max_cache_size") == 5

    res = sync_engine.update_config("max_cache_size", 10)
    assert res["status"] == "synchronized"
    assert sync_engine.get_config("max_cache_size") == 10

    err_res = sync_engine.update_config("non_existent_key", 99)
    assert err_res["status"] == "error"
