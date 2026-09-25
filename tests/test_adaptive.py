from app.core.adaptive_learning import AdaptiveLearningEngine

def test_adaptive_learning():
    engine = AdaptiveLearningEngine()
    pattern = "ankara trafik"
    
    engine.register_pattern(pattern, initial_weight=1.0)
    
    # Apply positive feedback -> weight should increase
    res_pos = engine.apply_feedback(pattern, is_positive=True)
    assert res_pos["updated_weight"] > 1.0
    assert res_pos["status"] == "adapted"

    # Apply negative feedback -> weight should decrease
    res_neg = engine.apply_feedback(pattern, is_positive=False)
    assert res_neg["updated_weight"] < res_pos["updated_weight"]
