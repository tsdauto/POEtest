from ..Invokers.TestInvoker import TestInvoker
from ..commands.LogoutCommand import LogoutCommand


def run(crt_env):
    try:
        logout_command = LogoutCommand(crt_env)

        test_invoker = TestInvoker()

        test_invoker.addCommand(logout_command)

        test_invoker.run()

    except Exception as e:

        return False
