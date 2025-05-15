from config1 import COM_PORT
from .Command import Command
from typing import Optional

class PoeCommand(Command):
    def __init__(self, crtEnv, username: str = "admin", password: str = "admin", command: str = "", port: str = "COM9"):
        self.__crtEnv = crtEnv
        self.__username = username
        self.__password = password
        self.__command = command
        self.__port = port

    def execute(self) -> Optional[str]:
            self.__crtEnv.switch_port(self.__port)
            self.__crtEnv.sleep(2)
            self.__crtEnv.send('\n')
            self.__crtEnv.waitForString(['login...', 'ame:', '#'], 200)
            self.__crtEnv.send('\n')
            self.__crtEnv.waitForString(['ame:', '#'], 200)
            self.__crtEnv.sleep(1)
            self.__crtEnv.send(self.__username)
            self.__crtEnv.waitForString(['assword:', '#'], 200)
            self.__crtEnv.sleep(1)
            self.__crtEnv.send(self.__password)
            self.__crtEnv.sleep(10)
            self.__crtEnv.send(self.__command)
            self.__crtEnv.sleep(1)
            self.__crtEnv.waitForString('#', 200)
            self.__crtEnv.send('exit\n')
            