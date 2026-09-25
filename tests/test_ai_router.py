
import time
from app.ai.router import ProviderHealth

def test_provider_health_initial_state():
    ph = ProviderHealth("OpenAI", cooldown_seconds=1)
    assert ph.name == "OpenAI"
    assert ph.available is True
    assert ph.failures == 0

def test_provider_health_failure_and_cooldown():
    ph = ProviderHealth("Groq", cooldown_seconds=1)
    ph.record_failure()
    assert ph.available is False
    assert ph.failures == 1

    # Wait for cooldown expiration
    time.sleep(1.1)
    assert ph.check_cooldown() is True
    assert ph.available is True
