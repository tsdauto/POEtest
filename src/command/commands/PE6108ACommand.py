from command.serial_env.TelnetEnv import TelnetEnv

class PE6108ACommand:
    def __init__(self, telnet_env, command):
        self.telnet_env = telnet_env
        self.username = "administrator"
        self.password = "password"
        self.command = command

    def execute(self):
        tn = self.telnet_env
        tn.read_until(b'Login:')  # 等待 Username prompt
        tn.send(self.username)
        tn.read_until(b'Password:')  # 等待 Password prompt
        tn.send(self.password)
        tn.read_until(b'>')  # 等待登入成功的 prompt
        tn.send(self.command)
        tn.read_until(b'>')
        tn.close()