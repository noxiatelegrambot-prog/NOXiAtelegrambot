from app.core.memory_optimizer import MemoryOptimizer

def test_memory_optimizer_cache_limit():
    optimizer = MemoryOptimizer(max_cache_size=3)
    
    optimizer.add_to_cache({"id": 1})
    optimizer.add_to_cache({"id": 2})
    optimizer.add_to_cache({"id": 3})
    assert len(optimizer.cache) == 3

    # Adding a 4th item should trigger pruning of the oldest (id: 1)
    optimizer.add_to_cache({"id": 4})
    assert len(optimizer.cache) == 3
    assert optimizer.cache[0]["id"] == 2

    opt_res = optimizer.optimize_memory()
    assert opt_res["status"] == "optimized"
    assert opt_res["current_cache_size"] == 3
