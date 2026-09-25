from app.core.architecture_audit import ArchitectureAudit

def test_module_inventory():
    res = ArchitectureAudit.inventory_modules()
    assert res["total_python_modules"] > 0
    assert res["status"] == "inventory_clean"

def test_dependency_scan():
    res = ArchitectureAudit.check_circular_dependencies()
    assert res["circular_dependencies_found"] == 0
    assert res["status"] == "dependency_graph_stable"
