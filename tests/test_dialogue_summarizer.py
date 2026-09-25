from app.core.dialogue_summarizer import DialogueSummarizer

def test_dialogue_summarizer():
    summarizer = DialogueSummarizer()
    summarizer.add_message("User", "Ankara trafik nasıl?")
    summarizer.add_message("NOXiA", "Metro hatları aktif.")
    summarizer.add_message("User", "Teşekkürler.")

    summary = summarizer.generate_summary()
    assert summary["total_messages"] == 3
    assert summary["unique_participants"] == 2
    assert "Ankara trafik" in summary["summary"]
