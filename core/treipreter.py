## Interpreter of Treiscript

from . import *

def treipreter(code='',dx=32):
  if code=='':
    code = 'd_cons_pi'
  d = eval(code)
  return d
