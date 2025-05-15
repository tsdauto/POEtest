from .Command import Command
from typing import Optional

class RT_PoE5Command(Command):
    def __init__(self, crtEnv, command: str, port: str = "COM10"):
        self.__crtEnv = crtEnv
        self.__command = command
        self.__port = port

    def execute(self) -> Optional[str]:
            self.__crtEnv.switch_port(self.__port)
            self.__crtEnv.send('\r')
            self.__crtEnv.waitForString('RT-PoE5>', 200)
            self.__crtEnv.sleep(1)
            self.__crtEnv.send(self.__command)
            self.__crtEnv.sleep(1)
            self.__crtEnv.waitForString('RT-PoE5>', 200)