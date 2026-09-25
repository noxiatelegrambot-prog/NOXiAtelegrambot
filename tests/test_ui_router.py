from app.core.ui_router import UIStateRouter

def test_ui_screens():
    main_res = UIStateRouter.render_screen("main")
    assert main_res["status"] == "success"
    assert "Ana Ekran" in main_res["content"]["title"]

    research_res = UIStateRouter.render_screen("research")
    assert research_res["content"]["title"] == "🔍 Araştır Ekranı"

    unknown_res = UIStateRouter.render_screen("nonexistent")
    assert unknown_res["content"]["title"] == "Bilinmeyen Ekran"
