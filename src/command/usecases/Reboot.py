from ..Invokers.TestInvoker import  TestInvoker
from ..commands.Reboot import RebootCommand

def run(crt_env):

    logout_command = RebootCommand(crt_env)

    test_invoker = TestInvoker()

    test_invoker.addCommand(logout_command)

    test_invoker.run()

