from config1 import COM_PORT
from .Command import Command

class PoeCommand(Command):
    def __init__(self, crtEnv, username, password, command):
        self.__crtEnv = crtEnv
        self.__username = username
        self.__password = password
        self.__command = command

    def execute(self):
        self.__crtEnv.switch_port("COM4")
        self.__crtEnv.send('\n')
        self.__crtEnv.waitForString(['login...', 'ame:', '#'], 200)
        self.__crtEnv.send('\n')
        self.__crtEnv.waitForString(['ame:', '#'], 200)
        self.__crtEnv.sleep(1)
        self.__crtEnv.send(self.__username)
        self.__crtEnv.waitForString(['assword:', '#'], 200)
        self.__crtEnv.sleep(1)
        self.__crtEnv.send(self.__password)
        self.__crtEnv.send(self.__command)
        self.__crtEnv.waitForString('#', 200)
        self.__crtEnv.sleep(1)
        self.__crtEnv.send('exit\n')

        # 取得最近的 console 輸出
        output = ''.join(list(self.__crtEnv.buffer))
        for line in output.splitlines():
            if "eth1/0/1" in line:
                return line
        return None