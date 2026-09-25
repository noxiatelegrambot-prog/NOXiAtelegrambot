def format_dashboard_header(status: str, active_tasks: int, memory_count: int) -> str:
    return (
        "🤖 **NOXiA Operational Control Center**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🟢 **System Status:** {status}\n"
        f"⚡ **Active Tasks:** {active_tasks}\n"
        f"🧠 **Memories Stored:** {memory_count}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Select a module below to inspect or manage:"
    )
