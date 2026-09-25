from app.ui.navigation import NavigationStack
from app.ui.keyboards import get_main_dashboard_keyboard, CB_NEW_TASK
from app.ui.screens import render_start_screen
from app.ui.pagination import paginate_items

def test_navigation_stack():
    nav = NavigationStack()
    assert nav.current() == "main"
    nav.push("tasks")
    assert nav.current() == "tasks"
    nav.push("task_detail")
    assert nav.current() == "task_detail"
    # pop() removes task_detail and returns the new current state (tasks)
    assert nav.pop() == "tasks"
    assert nav.current() == "tasks"

def test_keyboards_structure():
    kb = get_main_dashboard_keyboard()
    flat_callbacks = [cb for row in kb for _, cb in row]
    assert CB_NEW_TASK in flat_callbacks

def test_screen_rendering():
    text = render_start_screen("Operational", 3, 42)
    assert "NOXiA Operational Control Center" in text
    assert "Active Tasks:" in text
    assert "3" in text
    assert "Memories Stored:" in text
    assert "42" in text

def test_pagination():
    items = list(range(12))
    page1, has_next = paginate_items(items, page=1, page_size=5)
    assert len(page1) == 5
    assert page1 == [0, 1, 2, 3, 4]
    assert has_next is True

from app.ui.keyboards import get_task_type_keyboard, CB_TASK_RESEARCH, get_task_confirmation_keyboard, CB_TASK_START
from app.ui.screens import render_new_task_screen, render_task_summary_screen, render_task_status_screen

def test_task_center_keyboards():
    kb = get_task_type_keyboard()
    flat_cbs = [cb for row in kb for _, cb in row]
    assert CB_TASK_RESEARCH in flat_cbs

    conf_kb = get_task_confirmation_keyboard()
    flat_conf_cbs = [cb for row in conf_kb for _, cb in row]
    assert CB_TASK_START in flat_conf_cbs

def test_task_center_screens():
    new_screen = render_new_task_screen()
    assert "New Task Center" in new_screen

    summary = render_task_summary_screen("Research", "Analyze Ankara public transport")
    assert "Research" in summary
    assert "Ankara public transport" in summary

    status_scr = render_task_status_screen("99", "Running", "Researcher")
    assert "ID: 99" in status_scr
    assert "Running" in status_scr
    assert "Researcher" in status_scr

from app.ui.keyboards import get_active_task_detail_keyboard, CB_TASK_CANCEL_ACTION
from app.ui.screens import render_active_tasks_screen, render_task_detail_screen

def test_active_tasks_keyboards():
    kb = get_active_task_detail_keyboard(101)
    flat_cbs = [cb for row in kb for _, cb in row]
    assert f"{CB_TASK_CANCEL_ACTION}_101" in flat_cbs

def test_active_tasks_screens():
    empty_scr = render_active_tasks_screen([])
    assert "No active tasks" in empty_scr

    sample_tasks = [{"id": 1, "title": "Analyze DB", "status": "running"}]
    list_scr = render_active_tasks_screen(sample_tasks)
    assert "Analyze DB" in list_scr
    assert "ID 1" in list_scr

    detail_scr = render_task_detail_screen(1, "Analyze DB", "running", "Step 1 -> Step 2", "12s", "Developer")
    assert "Analyze DB" in detail_scr
    assert "Step 1 -> Step 2" in detail_scr
    assert "12s" in detail_scr
