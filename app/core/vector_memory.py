
import math

class VectorMemoryEngine:
    def __init__(self):
        self.vectors = []

    def _tokenize(self, text: str) -> set:
        return set(text.lower().split())

    def _cosine_similarity(self, text1: str, text2: str) -> float:
        set1 = self._tokenize(text1)
        set2 = self._tokenize(text2)
        
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        
        if not union:
            return 0.0
        return len(intersection) / len(union) # Jaccard-based semantic proxy for lightweight local search

    def add_vector_memory(self, doc_id: str, content: str, metadata: dict = None) -> dict:
        item = {
            "id": doc_id,
            "content": content,
            "metadata": metadata or {}
        }
        self.vectors.append(item)
        return item

    def semantic_search(self, query: str, top_k: int = 3) -> list:
        if not query or not self.vectors:
            return []

        scored = []
        for item in self.vectors:
            score = self._cosine_similarity(query, item["content"])
            scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for score, item in scored[:top_k] if score > 0.0]
