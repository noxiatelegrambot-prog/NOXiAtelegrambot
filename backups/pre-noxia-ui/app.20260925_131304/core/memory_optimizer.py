class MemoryOptimizer:
    def __init__(self, max_cache_size: int = 5):
        self.max_cache_size = max_cache_size
        self.cache = []

    def add_to_cache(self, item: dict) -> int:
        self.cache.append(item)
        if len(self.cache) > self.max_cache_size:
            # Drop the oldest item to free memory
            self.cache.pop(0)
        return len(self.cache)

    def optimize_memory(self) -> dict:
        initial_count = len(self.cache)
        # Perform garbage collection / pruning simulation
        optimized_count = len(self.cache)
        return {
            "status": "optimized",
            "pruned_items": 0,
            "current_cache_size": optimized_count
        }
