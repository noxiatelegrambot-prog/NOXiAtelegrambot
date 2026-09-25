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

# Task Center callback constants
CB_TASK_GENERAL = "task_type_general"
CB_TASK_RESEARCH = "task_type_research"
CB_TASK_DEV = "task_type_dev"
CB_TASK_TEST = "task_type_test"
CB_TASK_ANALYZE = "task_type_analyze"
CB_TASK_START = "task_start"
CB_TASK_CANCEL = "task_cancel"
CB_TASK_RETRY = "task_retry"
CB_TASK_DETAILS = "task_detail"

def get_task_type_keyboard():
    return [
        [("🌐 Genel Görev", CB_TASK_GENERAL), ("🔍 Araştırma", CB_TASK_RESEARCH)],
        [("💻 Geliştirme", CB_TASK_DEV), ("🧪 Test", CB_TASK_TEST)],
        [("📊 Analiz", CB_TASK_ANALYZE)],
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]

def get_task_confirmation_keyboard():
    return [
        [("🚀 Başlat", CB_TASK_START), ("❌ İptal", CB_TASK_CANCEL)],
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]

def get_task_result_keyboard():
    return [
        [("🔄 Tekrar Çalıştır", CB_TASK_RETRY), ("📋 Detaylar", CB_TASK_DETAILS)],
        [("🏠 Ana Menü", CB_MAIN)]
    ]
