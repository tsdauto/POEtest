from ..Invokers.TestInvoker import TestInvoker
from ..commands.ResetCommand import ResetCommand


def run(crtEnv):
    try:
        resetCommand = ResetCommand(crtEnv)

        testInvoker = TestInvoker()

        testInvoker.addCommand(resetCommand)

        testInvoker.run()

    except Exception as e:

        return False
