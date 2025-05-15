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
        lines = []
        for line in output.splitlines():
            if "eth1/0/1" in line:
                lines.append(line)
        if lines:
            header = "Interface   State          Class     Max(W)    Used(W)   Description\n" \
                     "------------------------------------------------------------------------------------------\n"
            return header + "\n".join(lines)
        return None

    except Exception as e:
        return False