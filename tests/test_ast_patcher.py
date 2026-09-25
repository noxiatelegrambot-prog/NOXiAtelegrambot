from app.core.ast_patcher import ASTCodePatcher

def test_ast_code_patcher_validation():
    patcher = ASTCodePatcher()
    valid_code = "def sample_func():\n    return True"
    invalid_code = "def broken_func(:\n    return"

    assert patcher.validate_python_code(valid_code) is True
    assert patcher.validate_python_code(invalid_code) is False

    funcs = patcher.inspect_functions(valid_code)
    assert "sample_func" in funcs

    res = patcher.safe_patch_apply("old", valid_code)
    assert res["status"] == "applied"
