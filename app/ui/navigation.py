class NavigationStack:
    def __init__(self):
        self.stack = []

    def push(self, state: str):
        if not self.stack or self.stack[-1] != state:
            self.stack.append(state)

    def pop(self) -> str:
        if len(self.stack) > 1:
            return self.stack.pop()
        return self.stack[0] if self.stack else "main"

    def current(self) -> str:
        return self.stack[-1] if self.stack else "main"

    def clear(self):
        self.stack = ["main"]
