import os

class DeveloperAgent:
    @staticmethod
    def write_code_to_sandbox(sandbox_path: str, filename: str, code_content: str) -> dict:
        try:
            file_path = os.path.join(sandbox_path, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code_content)
            return {
                "status": "success",
                "file_path": file_path,
                "bytes_written": len(code_content)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    @staticmethod
    def generate_module_scaffold(module_name: str) -> str:
        return f'''# Auto-generated module: {module_name}

class {module_name.capitalize()}:
    def __init__(self):
        self.name = "{module_name}"

    def run(self) -> dict:
        return {{"status": "success", "module": self.name}}
'''
