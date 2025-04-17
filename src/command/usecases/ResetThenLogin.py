from ..Invokers import TestInvoker
from ..commands.LoginCommand import LoginCommand
from  ..commands.ResetCommand import ResetCommand
from ..config import CONFIG


def run(crt_env):
    try:
        # init command
        reset_command = ResetCommand(crt_env)

        login_command = LoginCommand(crt_env, CONFIG['ADMIN_USER_ACCOUNT'], CONFIG['ADMIN_USER_PASSWORD'])

        test_invoker = TestInvoker.TestInvoker()

        # add to task queue
        test_invoker.addCommand(reset_command)

        test_invoker.addCommand(login_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False
