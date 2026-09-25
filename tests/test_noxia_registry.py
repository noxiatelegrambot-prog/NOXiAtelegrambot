from app.core.noxia_registry import NoxiaRegistry

def test_command_prefix_standardization():
    assert NoxiaRegistry.get_command("start") == "noxia_start"
    assert NoxiaRegistry.get_command("help") == "noxia_help"
    assert NoxiaRegistry.get_command("status") == "noxia_status"
    assert "research" in NoxiaRegistry.SUBMENUS
    assert "Yeni Geliştirme" in NoxiaRegistry.SUBMENUS["dev"]
