class SelfCorrectionAgent:
    @staticmethod
    def analyze_failure(error_output: str) -> dict:
        error_lower = error_output.lower()
        if "assertionerror" in error_lower:
            diagnosis = "Test assertion failed. Expected output did not match actual result."
            suggestion = "Review test expectations or adjust logic to meet assertions."
        elif "syntaxerror" in error_lower:
            diagnosis = "Python syntax error detected in generated code."
            suggestion = "Fix syntax, check indentation and missing colons or parentheses."
        elif "modulenotfounderror" in error_lower:
            diagnosis = "Missing dependency or incorrect import path."
            suggestion = "Ensure required packages are installed or correct the import statement."
        else:
            diagnosis = "Unknown execution or runtime error."
            suggestion = "Inspect traceback and add defensive error handling."

        return {
            "status": "success",
            "diagnosis": diagnosis,
            "suggestion": suggestion,
            "requires_retry": True
        }
