from app.core.self_correction_agent import SelfCorrectionAgent

def test_self_correction_analysis():
    mock_traceback = "E       AssertionError: assert 3 == 4\nE         - 4\nE         + 3"
    res = SelfCorrectionAgent.analyze_failure(mock_traceback)
    assert res["status"] == "success"
    assert "assertion" in res["diagnosis"].lower()
    assert res["requires_retry"] is True

    mock_syntax = "SyntaxError: invalid syntax"
    res_syntax = SelfCorrectionAgent.analyze_failure(mock_syntax)
    assert "syntax" in res_syntax["diagnosis"].lower()
