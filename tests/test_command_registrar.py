from app.core.command_registrar import CommandRegistrar
from app.core.noxia_registry import NoxiaRegistry

def test_telegram_commands_payload():
    payload = CommandRegistrar.get_telegram_commands_payload()
    assert isinstance(payload, list)
    assert len(payload) >= 7
    
    commands = [c["command"] for c in payload]
    assert NoxiaRegistry.COMMANDS["start"] in commands
    assert NoxiaRegistry.COMMANDS["bulmaca"] in commands

def test_command_menu_text():
    text = CommandRegistrar.format_command_menu_text()
    assert "NOXiA Komut Listesi" in text
    assert "noxia_start" in text
