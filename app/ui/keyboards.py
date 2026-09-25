CB_MAIN = "menu_main"
CB_NEW_TASK = "menu_new_task"
CB_TASKS = "menu_tasks"
CB_MEMORY = "menu_memory"
CB_AI_HUB = "menu_ai_hub"
CB_RESEARCH = "menu_research"
CB_DEVELOPER = "menu_developer"
CB_TEST_CENTER = "menu_test_center"
CB_SETTINGS = "menu_settings"
CB_SYSTEM = "menu_system"
CB_BACK = "menu_back"

def get_main_dashboard_keyboard():
    return [
        [("🚀 Yeni Görev", CB_NEW_TASK), ("📋 Görevler", CB_TASKS)],
        [("🧠 Memory", CB_MEMORY), ("⚡ AI Merkezi", CB_AI_HUB)],
        [("🔍 Araştırma", CB_RESEARCH), ("💻 Geliştirici", CB_DEVELOPER)],
        [("🧪 Test Merkezi", CB_TEST_CENTER), ("⚙️ Sistem", CB_SYSTEM)],
        [("🛠️ Ayarlar", CB_SETTINGS)]
    ]

def get_back_navigation_keyboard():
    return [
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]
