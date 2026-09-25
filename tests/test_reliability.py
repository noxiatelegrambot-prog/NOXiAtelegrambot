from app.core.reliability_manager import ReliabilityManager

def test_safe_error_formatting():
    raw_error = "Traceback (most recent call last): DB connection timeout at 0x1234"
    safe = ReliabilityManager.format_safe_error(raw_error)
    assert "Traceback" not in safe
    assert "⚠️" in safe

def test_message_chunking():
    long_text = "A" * 5000
    chunks = ReliabilityManager.chunk_long_message(long_text, max_length=2000)
    assert len(chunks) == 3
    assert len(chunks[0]) == 2000
    assert len(chunks[2]) == 1000
