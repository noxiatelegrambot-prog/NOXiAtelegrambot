import ast

class ASTCodePatcher:
    def __init__(self):
        self.last_parsed_tree = None

    def validate_python_code(self, code_str: str) -> bool:
        try:
            self.last_parsed_tree = ast.parse(code_str)
            return True
        except SyntaxError:
            return False

    def inspect_functions(self, code_str: str) -> list:
        if not self.validate_python_code(code_str):
            return []
        
        functions = []
        for node in ast.walk(self.last_parsed_tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
        return functions

    def safe_patch_apply(self, original_code: str, new_code: str) -> dict:
        if not self.validate_python_code(new_code):
            return {"status": "rejected", "reason": "Syntax error in patch code."}
        return {"status": "applied", "code": new_code}
