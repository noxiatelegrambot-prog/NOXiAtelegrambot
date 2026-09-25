from app.core.semantic_matcher import SemanticMatcher

def test_semantic_cosine_matching():
    matcher = SemanticMatcher()
    kb = [
        "Ankara'da ulaşım ve metro hatları",
        "Telegram bot otonom görev yönetimi",
        "Sistem telemetri ve performans metrikleri"
    ]

    result = matcher.find_best_match("Ankara metro hatları nasıl", kb)
    assert result["best_match"] == "Ankara'da ulaşım ve metro hatları"
    assert result["similarity_score"] > 0.0
