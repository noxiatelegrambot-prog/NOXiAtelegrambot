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

def render_learning_hub_screen(total_exp: int, success_count: int, failure_count: int) -> str:
    return (
        "💡 **Learning & Experience Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📚 **Total Experiences:** {total_exp}\n"
        f"✅ **Successful Solutions:** {success_count}\n"
        f"❌ **Recorded Failures:** {failure_count}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Inspect what NOXiA learned from past executions:"
    )

def render_learning_failures_screen(failures: list) -> str:
    if not failures:
        return (
            "❌ **Recent Failures**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🟢 No recent failures recorded."
        )
    listing = "\n".join([f"• **Task #{f.get("task_id")}**: {f.get("lesson")}" for f in failures])
    return (
        "❌ **Recent Failures & Lessons**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{listing}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

def render_research_hub_screen() -> str:
    return (
        "🔍 **Research Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Enter a topic or query to initiate deep multi-source research:"
    )

def render_research_results_screen(topic: str, sources: list, summary: str) -> str:
    if not sources:
        sources_text = "No sources found."
    else:
        sources_text = "\n".join([f"• [{s.get("title")}]({s.get("url")}) — *{s.get("domain")}*" for s in sources])

    return (
        f"🔍 **Research Results: {topic}**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📄 **Summary:**\n{summary}\n\n"
        f"🌐 **Sources ({len(sources)}):**\n{sources_text}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

def render_dev_hub_screen() -> str:
    return (
        "💻 **Development & Code Analysis Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Select an operation to review repository health, check syntax, or apply automated patches:"
    )

def render_code_analysis_screen(filename: str, issues_count: int, quality_score: int, suggestions: list) -> str:
    if not suggestions:
        sug_text = "No refactoring suggestions."
    else:
        sug_text = "\n".join([f"• {s}" for s in suggestions])

    return (
        f"💻 **Code Analysis: {filename}**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⚠️ **Issues Found:** {issues_count}\n"
        f"⭐ **Quality Score:** {quality_score}/100\n\n"
        f"💡 **Suggestions:**\n{sug_text}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
