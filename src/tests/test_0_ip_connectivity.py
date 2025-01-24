import socket
import pytest
from dotenv import load_dotenv
import os

load_dotenv()

http_port = os.getenv("HTTP_PORT")
tls_port = os.getenv("TLS_PORT")


def is_ip_reachable(ip, port, timeout=3):
    """檢查 IP 是否可以連線"""
    try:
        with socket.create_connection((ip, port), timeout):
            return True
    except (socket.timeout, socket.error):
        return False

@pytest.mark.parametrize("ip, port", [
    # ("10.90.90.90", tls_port),
    ("10.90.90.90", http_port),  
])
def test_ip_connectivity(ip, port):
    assert is_ip_reachable(ip, port), f"無法連接到 {ip}:{port}"
