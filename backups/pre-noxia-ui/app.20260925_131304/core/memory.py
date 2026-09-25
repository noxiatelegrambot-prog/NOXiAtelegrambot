
import time

class MemoryEngine:
    def __init__(self):
        self.memories = []
        self.categories = {"experience", "knowledge", "decision", "lesson", "preference", "error"}

    def add_memory(self, category: str, content: str, importance: int = 1, confidence: float = 1.0) -> dict:
        if category not in self.categories:
            raise ValueError(f"Invalid memory category: {category}")
        
        memory_item = {
            "id": len(self.memories) + 1,
            "category": category,
            "content": content,
            "importance": importance,
            "confidence": confidence,
            "timestamp": time.time()
        }
        self.memories.append(memory_item)
        return memory_item

    def search_memories(self, query: str, category: str = None) -> list:
        if not query:
            return []
        
        query_lower = query.lower()
        results = []
        for mem in self.memories:
            if category and mem["category"] != category:
                continue
            if query_lower in mem["content"].lower():
                results.append(mem)
        return results
