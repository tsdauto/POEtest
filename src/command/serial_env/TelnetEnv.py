import telnetlib
import time

class TelnetEnv:
    def __init__(self, host, port=23, timeout=10, encoding='utf-8'):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.encoding = encoding
        self.tn = telnetlib.Telnet()
        self.connect()

    def connect(self):
        self.tn.open(self.host, self.port, self.timeout)
        print(f"✅ Telnet connected on {self.host}:{self.port}")

    def send(self, cmd, wait=0.2):
        if not cmd.endswith('\r\n'):
            cmd += '\r\n'
        print(f"[Telnet SEND] {cmd.strip()}")
        self.tn.write(cmd.encode(self.encoding))
        time.sleep(wait)

    def read_until(self, expected=b'>', timeout=5):
        data = self.tn.read_until(expected, timeout)
        try:
            decoded = data.decode(self.encoding)
            print(f"[Telnet RECV] {decoded.strip()}")
            return decoded
        except Exception:
            print(f"[Telnet RECV] {data}")
            return data

    def interactive(self, prompt=b'>', timeout=1):
        """持續讀取並即時輸出 telnet 畫面，直到遇到 prompt 或超時"""
        while True:
            data = self.tn.read_until(prompt, timeout)
            try:
                decoded = data.decode(self.encoding)
                print(decoded, end='')
            except Exception:
                print(data, end='')
            if prompt in data:
                break

    def close(self):
        self.tn.close()
        print("🔌 Telnet closed") 