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

# Active Tasks callback constants
CB_TASK_CANCEL_ACTION = "task_action_cancel"
CB_TASK_RESUME_ACTION = "task_action_resume"
CB_TASK_HISTORY = "task_history_list"

def get_active_task_detail_keyboard(task_id: int):
    return [
        [("🛑 İptal Et", f"{CB_TASK_CANCEL_ACTION}_{task_id}"), ("▶️ Devam Et", f"{CB_TASK_RESUME_ACTION}_{task_id}")],
        [("📜 Geçmiş", CB_TASK_HISTORY), ("⬅️ Geri", CB_BACK)],
        [("🏠 Ana Menü", CB_MAIN)]
    ]

# AI Hub callback constants
CB_AI_TEST_CONNECTION = "ai_test_connection"
CB_AI_TOGGLE_PROVIDER = "ai_toggle_provider"
CB_AI_CHAIN_VIEW = "ai_chain_view"

def get_ai_hub_keyboard():
    return [
        [("🧪 Bağlantıyı Test Et", CB_AI_TEST_CONNECTION), ("🔄 Fallback Zinciri", CB_AI_CHAIN_VIEW)],
        [("⚙️ Sağlık & Metrikler", "ai_metrics_view"), ("⬅️ Geri", CB_BACK)],
        [("🏠 Ana Menü", CB_MAIN)]
    ]

# Memory Center callback constants
CB_MEM_SEARCH = "memory_search"
CB_MEM_LIST = "memory_list"
CB_MEM_DELETE = "memory_delete"

def get_memory_hub_keyboard():
    return [
        [("🔍 Bellek Ara", CB_MEM_SEARCH), ("📚 Tüm Bellekler", CB_MEM_LIST)],
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]

def get_memory_detail_keyboard(memory_id: int):
    return [
        [("🗑️ Sil", f"{CB_MEM_DELETE}_{memory_id}")],
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]

# Learning Center callback constants
CB_LEARN_STATS = "learning_stats"
CB_LEARN_ERRORS = "learning_errors"
CB_LEARN_SOLUTIONS = "learning_solutions"

def get_learning_hub_keyboard():
    return [
        [("📊 Öğrenme İstatistikleri", CB_LEARN_STATS), ("❌ Son Hatalar", CB_LEARN_ERRORS)],
        [("💡 Başarılı Çözümler", CB_LEARN_SOLUTIONS), ("⬅️ Geri", CB_BACK)],
        [("🏠 Ana Menü", CB_MAIN)]
    ]

# Research Center callback constants
CB_RES_START = "research_start_action"
CB_RES_SAVE = "research_save_memory"

def get_research_hub_keyboard():
    return [
        [("🔍 Araştırma Başlat", CB_RES_START)],
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]

def get_research_result_keyboard():
    return [
        [("💾 Belleğe Kaydet", CB_RES_SAVE)],
        [("⬅️ Geri", CB_BACK), ("🏠 Ana Menü", CB_MAIN)]
    ]

# Dev & Code Analysis callback constants
CB_DEV_ANALYZE = "dev_analyze_code"
CB_DEV_DIFF = "dev_view_diff"
CB_DEV_APPLY = "dev_apply_patch"

def get_dev_hub_keyboard():
    return [
        [("💻 Kod Analizi", CB_DEV_ANALYZE), ("📋 Diff Görüntüle", CB_DEV_DIFF)],
        [("🚀 Yama Uygula", CB_DEV_APPLY), ("⬅️ Geri", CB_BACK)],
        [("🏠 Ana Menü", CB_MAIN)]
    ]

# System Management callback constants
CB_SYS_LOGS = "system_view_logs"
CB_SYS_METRICS = "system_view_metrics"
CB_SYS_EMERGENCY_STOP = "system_emergency_stop"

def get_system_hub_keyboard():
    return [
        [("📜 Sistem Logları", CB_SYS_LOGS), ("📊 Sistem Metrikleri", CB_SYS_METRICS)],
        [("🛑 Acil Durdurma", CB_SYS_EMERGENCY_STOP), ("⬅️ Geri", CB_BACK)],
        [("🏠 Ana Menü", CB_MAIN)]
    ]
