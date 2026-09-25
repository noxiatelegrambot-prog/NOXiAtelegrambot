import sys
from app.core.exception_tracer import ExceptionTracer

def test_exception_tracer_workflow():
    tracer = ExceptionTracer()
    
    try:
        raise ValueError("Simulated critical system failure")
    except Exception:
        exc_type, exc_value, exc_tb = sys.exc_info()
        result = tracer.capture_exception(exc_type, exc_value, exc_tb)

    assert result["type"] == "ValueError"
    assert "Simulated critical system failure" in result["message"]
    assert result["status"] == "captured_and_analyzed"

    last_err = tracer.get_last_error()
    assert last_err["type"] == "ValueError"
