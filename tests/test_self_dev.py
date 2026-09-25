
import pytest
from app.core.self_dev import SelfDevelopmentManager

def test_self_development_patch_workflow():
    manager = SelfDevelopmentManager()
    patch = manager.propose_patch("app/core/controller.py", "# optimized code", "Performance boost")
    
    assert patch["status"] == "proposed"
    assert patch["id"] == 1

    success = manager.apply_patch(patch["id"])
    assert success is True
    assert manager.patch_history[0]["status"] == "applied"

    with pytest.raises(ValueError):
        manager.propose_patch("", "", "")
