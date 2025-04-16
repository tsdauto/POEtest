from ..Invokers.TestInvoker import TestInvoker
from ..commands.UserAccountsCommand import UserAccountsCommand

from ..utils.randomIP import randomIP
from ..config import CONFIG


def run(crtEnv):
    try:

        userAccountCommand = UserAccountsCommand(crtEnv)

        # must create an admin account first

        AdminAccount = [{"username": CONFIG['ADMIN_USER_ACCOUNT'], "accessRight": 'admin',
                         "password": CONFIG['ADMIN_USER_PASSWORD']}]

        userAccountCommand.createNewUserAccount(AdminAccount)

        userAccounts = [
            {"username": 'helloworld' + str(i), "accessRight": 'user', "password": CONFIG['ADMIN_USER_PASSWORD']} for i
            in range(1, 100)]

        userAccountCommand.createNewUserAccount(userAccounts)

        testInvoker = TestInvoker()

        testInvoker.addCommand(userAccountCommand)

        testInvoker.run()

    except Exception as e:

        return False
