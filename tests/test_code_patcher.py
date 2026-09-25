from app.core.code_patcher import SelfHealingPatcher

def test_self_healing_patcher():
    patcher = SelfHealingPatcher()
    
    unsafe_snippet = "result = eval('2 + 2')"
    result = patcher.analyze_and_patch(unsafe_snippet)

    assert result["is_patched"] is True
    assert "safe_eval_wrapper(" in result["patched_code"]
    assert result["status"] == "applied_safely"

    safe_snippet = "result = 2 + 2"
    result_safe = patcher.analyze_and_patch(safe_snippet)
    assert result_safe["is_patched"] is False
