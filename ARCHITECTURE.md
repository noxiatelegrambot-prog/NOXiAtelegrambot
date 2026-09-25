# NOXiA Architecture & System Analysis (Madde 26-50)

## Component Analysis
- **Core / Main**: `app/main.py` handles asynchronous event loops and bot entry.
- **Brain & Planner**: `app/brain/` manages orchestrator state and execution tasks.
- **Agents**: Specialized polymorphic agents (Researcher, Summarizer, Developer, Tester, Reviewer).
- **Memory**: SQLite-backed persistent memory and structured task history (`app/memory/`).
- **AI Router**: Multi-provider fallback and retry governance (`app/ai/`).
- **Security & Validation**: Strict Git-safe patch application and branch validation.
