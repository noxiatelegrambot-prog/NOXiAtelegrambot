class LLMGateway:
    def __init__(self):
        self.default_model = "gpt-4o"
        self.prompt_registry = {
            "analyzer": "Analyze the following user intent and classify tasks: {input}",
            "coder": "Write clean, modular Python code for: {input}"
        }

    def get_prompt(self, prompt_name: str, **kwargs) -> str:
        template = self.prompt_registry.get(prompt_name, "{input}")
        return template.format(**kwargs)

    def mock_completion(self, prompt_name: str, **kwargs) -> dict:
        prompt = self.get_prompt(prompt_name, **kwargs)
        return {
            "status": "success",
            "model": self.default_model,
            "prompt_used": prompt,
            "response": f"Mocked structured LLM response for [{prompt_name}]"
        }
