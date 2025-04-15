from ..Invokers.TestInvoker import  TestInvoker
from ..commands.ResetCommand import ResetCommand


def run(crtEnv):
  
  resetCommand = ResetCommand(crtEnv)
  
  testInvoker = TestInvoker()
  
  testInvoker.addCommand(resetCommand)
  
  testInvoker.run()

