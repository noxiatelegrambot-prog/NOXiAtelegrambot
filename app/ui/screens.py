from app.ui.formatting import format_dashboard_header

def render_start_screen(status="Operational", active_tasks=0, memory_count=0) -> str:
    return format_dashboard_header(status, active_tasks, memory_count)
