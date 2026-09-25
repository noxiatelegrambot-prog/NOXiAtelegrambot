# NOXiA: Autonomous Multi-Agent Telegram Bot System

NOXiA is a modular, asynchronous, SQLite-backed multi-agent system integrated with Telegram. It leverages specialized polymorphic agents (Orchestrator, Researcher, Summarizer) governed by a robust asynchronous event loop, complete audit trails, performance metrics, and CI/CD pipelines.

## Architecture
- **Core Engine**: Asynchronous Python (`asyncio`, `aiosqlite`)
- **Memory & Audit Trail**: SQLite store (`noxia.db`) with structured memories and agent run logs.
- **Agents**: Polymorphic architecture supporting specialized task execution and fallback routing.
- **Interface**: Telegram Bot service (`BotService`, `TelegramBotHandler`).
- **Deployment**: Dockerized with automated GitHub Actions CI/CD testing.

## Running Tests
\`\`\`bash
python -m pytest -q tests
\`\`\`

## Running the Bot
\`\`\`bash
python main.py
\`\`\`
