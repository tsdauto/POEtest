from ..Invokers.TestInvoker import TestInvoker
from ..commands.RT_PoE5Command import RT_PoE5Command

def run(crt_env):
    try:
        poe_command = RT_PoE5Command(
            crt_env,
            'pwr 5\r'
        )

        test_invoker = TestInvoker()
        test_invoker.addCommand(poe_command)
        test_invoker.run()

        # 取得最近的 console 輸出
        output = ''.join(list(crt_env.buffer))
        for line in output.splitlines():
            if ":p1 2W" in line:
                return line
        return True

    except Exception as e:
        return False

def run2(crt_env):
    try:
        poe_command = RT_PoE5Command(
            crt_env,
            'getp\r'
        )

        test_invoker = TestInvoker()
        test_invoker.addCommand(poe_command)
        test_invoker.run()

        # 取得最近的 console 輸出
        output = ''.join(list(crt_env.buffer))
        for line in output.splitlines():
            if ":p1 2W" in line:
                return line
        return True

    except Exception as e:
        return False

def run3(crt_env):
    try:
        poe_command = RT_PoE5Command(
            crt_env,
            'pwr 0\r'
        )

        test_invoker = TestInvoker()
        test_invoker.addCommand(poe_command)
        test_invoker.run()

        return True

    except Exception as e:
        return False