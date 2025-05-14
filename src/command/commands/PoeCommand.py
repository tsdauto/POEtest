from config1 import COM_PORT
from .Command import Command
from typing import Optional

class PoeCommand(Command):
    def __init__(self, crtEnv, username: str = "admin", password: str = "admin", command: str = "", port: str = "COM4"):
        self.__crtEnv = crtEnv
        self.__username = username
        self.__password = password
        self.__command = command
        self.__port = port

    def execute(self) -> Optional[str]:
        try:
            self.__crtEnv.switch_port(self.__port)
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
            self.__crtEnv.sleep(1)
            self.__crtEnv.waitForString('#', 200)
            self.__crtEnv.send('exit\n')

            output = ''.join(list(self.__crtEnv.buffer))
            for line in output.splitlines():
                if "eth1/0/1" in line:
                    return line
            return None
        except Exception as e:
            print(f"[PoeCommand] 執行失敗: {e}")
            return None