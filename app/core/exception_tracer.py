import traceback
import sys

class ExceptionTracer:
    def __init__(self):
        self.error_logs = []

    def capture_exception(self, exc_type, exc_value, exc_tb) -> dict:
        tb_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        error_item = {
            "type": exc_type.__name__,
            "message": str(exc_value),
            "traceback": tb_str,
            "status": "captured_and_analyzed"
        }
        self.error_logs.append(error_item)
        return error_item

    def get_last_error(self) -> dict:
        if not self.error_logs:
            return None
        return self.error_logs[-1]
