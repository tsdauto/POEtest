import random

from ..commands.QinQCommand import QinQCommand
from ..Invokers.TestInvoker import TestInvoker


def run(crtEnv):
    try:
        qinQCommand = QinQCommand(crtEnv)

        replaceVidLists = [
            {'action': 'replace', 'svid': str(i + 1), 'cvid': str(i + 1), 'priority': str(random.randint(1, 7))} for i
            in range(1, 1000)]

        actionVidLists = [
            {'action': 'add', 'svid': str(i + 1), 'cvid': str(i + 1), 'priority': str(random.randint(1, 7))} for i in
            range(1001, 2000)]

        qinQCommand.addVlanTranslationCVID(replaceVidLists)

        qinQCommand.addVlanTranslationCVID(actionVidLists)

        testInvoker = TestInvoker()

        testInvoker.addCommand(qinQCommand)

        testInvoker.run()

    except Exception as e:

        return False
