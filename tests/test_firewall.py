from app.core.security_firewall import AutonomousFirewall

def test_autonomous_firewall():
    firewall = AutonomousFirewall()

    # Safe payload test
    res_safe = firewall.inspect_payload(123, "Merhaba NOXiA, nasılsın?")
    assert res_safe["is_safe"] is True
    assert res_safe["action"] == "allow"

    # Malicious payload test (SQL Injection / XSS)
    res_threat = firewall.inspect_payload(456, "SELECT * FROM users UNION SELECT password FROM admin")
    assert res_threat["is_safe"] is False
    assert res_threat["action"] == "block_and_flag"
    assert res_threat["threat"] is not None
