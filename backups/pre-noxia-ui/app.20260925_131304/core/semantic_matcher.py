import math
from collections import Counter

class SemanticMatcher:
    def _tokenize(self, text: str):
        return text.lower().strip().split()

    def _cosine_similarity(self, text1: str, text2: str) -> float:
        tokens1 = self._tokenize(text1)
        tokens2 = self._tokenize(text2)
        
        vec1 = Counter(tokens1)
        vec2 = Counter(tokens2)
        
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum(vec1[x] * vec2[x] for x in intersection)
        
        sum1 = sum(vec1[x] ** 2 for x in vec1)
        sum2 = sum(vec2[x] ** 2 for x in vec2)
        
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        
        if not denominator:
            return 0.0
        return float(numerator) / denominator

    def find_best_match(self, query: str, database_phrases: list) -> dict:
        best_match = None
        highest_score = 0.0
        
        for phrase in database_phrases:
            score = self._cosine_similarity(query, phrase)
            if score > highest_score:
                highest_score = score
                best_match = phrase
                
        return {
            "best_match": best_match,
            "similarity_score": round(highest_score, 4)
        }
