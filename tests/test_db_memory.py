from app.core.db_memory_manager import DatabaseMemoryManager
import os

def test_db_memory_manager():
    db = DatabaseMemoryManager("test_noxia.db")
    assert db.init_database() is True
    assert db.store_memory("test_key", "test_value") is True
    
    if os.path.exists("test_noxia.db"):
        os.remove("test_noxia.db")
