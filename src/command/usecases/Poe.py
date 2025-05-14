from ..Invokers.TestInvoker import TestInvoker
from ..commands.PoeCommand import PoeCommand

def run(crt_env):
    try:
        poe_command = PoeCommand(
            crt_env,
            'admin\n',
            'admin\n',
            'show poe power-inline interface ethernet 1/0/1 status\n'
        )

        test_invoker = TestInvoker()
        test_invoker.addCommand(poe_command)
        test_invoker.run()

        # 取得最近的 console 輸出
        output = ''.join(list(crt_env.buffer))
        for line in output.splitlines():
            if "eth1/0/1" in line:
                print("抓到的整行：", line)
                return line
        return None

    except Exception as e:
        return None