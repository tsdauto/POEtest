import sys
import os

def getScriptPath():
  return os.path.split(os.path.realpath(__file__))[0]

if getScriptPath() not in sys.path:
  sys.path.append(getScriptPath())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Invoker
reload(Invoker)

class Login(Invoker.Invoker):
  def __init__(self):
    super(Login, self).__init__()
    pass