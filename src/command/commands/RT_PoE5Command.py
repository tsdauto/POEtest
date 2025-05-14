

from .Command import Command

class RT_PoE5Command(Command):
    def __init__(self, crtEnv, command, command2):
        self.__crtEnv = crtEnv
        self.__command = command
        self.__command2 = command2

    def execute(self):
        self.__crtEnv.switch_port("COM3")
        self.__crtEnv.send('\r')
        self.__crtEnv.waitForString('RT-PoE5>', 200)
        self.__crtEnv.sleep(1)
        self.__crtEnv.send(self.__command)
        #self.__crtEnv.send('\r')
        self.__crtEnv.sleep(1)
        self.__crtEnv.waitForString('RT-PoE5>', 200)
        self.__crtEnv.send(self.__command2)
        #self.__crtEnv.send('\r')
        self.__crtEnv.sleep(2)
        self.__crtEnv.waitForString('RT-PoE5>', 200)
        
        # 取得最近的 console 輸出
        output = ''.join(list(self.__crtEnv.buffer))
        for line in output.splitlines():
            if ":p1 2W" in line:
                return line
        return None