from app.ui.formatting import format_dashboard_header

def render_start_screen(status="Operational", active_tasks=0, memory_count=0) -> str:
    return format_dashboard_header(status, active_tasks, memory_count)

def render_new_task_screen() -> str:
    return (
        "🚀 **New Task Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Select the category of the task you want to execute:"
    )

def render_task_summary_screen(task_type: str, prompt: str) -> str:
    return (
        "📋 **Task Execution Summary**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 **Type:** {task_type}\n"
        f"💬 **Prompt/Details:** {prompt}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Ready to dispatch to the orchestrator."
    )

def render_task_status_screen(task_id: str, status: str, agent: str = "Unassigned") -> str:
    return (
        f"⚡ **Task Status [ID: {task_id}]**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🔄 **Status:** {status}\n"
        f"🤖 **Assigned Agent:** {agent}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

def render_active_tasks_screen(tasks: list) -> str:
    if not tasks:
        return (
            "📋 **Active Tasks Center**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🟢 No active tasks currently running."
        )
    
    listing = "\n".join([f"• **ID {t.get("id")}**: {t.get("title")} [{t.get("status")}]" for t in tasks])
    return (
        "📋 **Active Tasks Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{listing}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Select a task to inspect details:"
    )

def render_task_detail_screen(task_id: int, title: str, status: str, plan: str, elapsed: str, agent: str) -> str:
    return (
        f"🔍 **Task Detail [ID: {task_id}]**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 **Title:** {title}\n"
        f"🔄 **Status:** {status}\n"
        f"🗺️ **Plan:** {plan}\n"
        f"⏱️ **Elapsed Time:** {elapsed}\n"
        f"🤖 **Agent:** {agent}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

def render_ai_hub_screen(providers: list) -> str:
    if not providers:
        return (
            "⚡ **AI Command Center**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🟢 No AI providers registered."
        )
    
    rows = []
    for p in providers:
        status_icon = "🟢" if p.get("available") else "🔴"
        rows.append(f"{status_icon} **{p.get("name")}** ({p.get("model")}) — Failures: {p.get("failures", 0)}")
    
    listing = "\n".join(rows)
    return (
        "⚡ **AI Command Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{listing}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Active Fallback Chain: OpenRouter ➔ Groq ➔ Gemini ➔ OpenAI"
    )

def render_ai_test_result_screen(provider: str, success: bool, latency_ms: float) -> str:
    status_text = "SUCCESS ✅" if success else "FAILED ❌"
    return (
        f"🧪 **AI Health Check [{provider}]**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Status: {status_text}\n"
        f"Latency: {latency_ms:.1f}ms\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

def render_memory_hub_screen(total_memories: int, total_experiences: int) -> str:
    return (
        "🧠 **Memory & Learning Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📦 **Total Memories:** {total_memories}\n"
        f"🎯 **Recorded Experiences:** {total_experiences}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Select an option to browse or search long-term storage:"
    )

def render_memory_detail_screen(memory_id: int, category: str, content: str, source: str) -> str:
    return (
        f"🧠 **Memory Detail [ID: {memory_id}]**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📂 **Category:** {category}\n"
        f"📝 **Content:** {content}\n"
        f"🔗 **Source:** {source}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
