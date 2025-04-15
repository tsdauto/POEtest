from.Command import Command

class ResetCommand(Command):
  def __init__(self, crtEnv):
    self.__crtEnv = crtEnv
  def execute(self):
    self.__crtEnv.send('')
    self.__crtEnv.send('')
    self.__crtEnv.send('reset')
    self.__crtEnv.waitForString('account?')
    self.__crtEnv.sleep(60000)
    self.__crtEnv.send('y')
    