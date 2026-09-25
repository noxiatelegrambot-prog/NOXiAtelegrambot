
from app.core.learning import LearningEngine

def test_learning_engine_evaluation():
    engine = LearningEngine()
    result = {"status": "success", "details": "all checks passed"}
    lesson = engine.evaluate_execution(result)
    
    assert lesson["type"] == "success_pattern"
    assert len(engine.get_insights()) == 1
