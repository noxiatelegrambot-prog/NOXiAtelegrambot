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
