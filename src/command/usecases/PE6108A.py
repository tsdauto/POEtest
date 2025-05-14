from ..commands.PE6108ACommand import PE6108ACommand

def run(telnet_env):
    try:
        PE6108A_cmd = PE6108ACommand(telnet_env,'sw o01 reboot\n')
        result = PE6108A_cmd.execute()
        return result
    except Exception as e:
        print("發生錯誤：", e)
        return False
