from command.serial_env.TelnetEnv import TelnetEnv
from typing import Optional

class PE6108ACommand:
    def __init__(self, telnet_env: TelnetEnv, command: str, username: str = "administrator", password: str = "password"):
        self.telnet_env = telnet_env
        self.username = username
        self.password = password
        self.command = command

    def execute(self) -> Optional[str]:
            tn = self.telnet_env
            tn.read_until(b'Login:')
            tn.send(self.username)
            tn.read_until(b'Password:')
            tn.send(self.password)
            tn.read_until(b'>')
            tn.send(self.command)
            result = tn.read_until(b'>')
            tn.close()