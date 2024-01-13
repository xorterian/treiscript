## Init and test formulas

from matplotlib import mathtext, font_manager
import matplotlib as mpl
mpl.rcParams['savefig.transparent'] = True
texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')

dx = 32

from visu import *
from core import *
from gui import *
import sys
 
if __name__=='__main__':
  print('Packages are processed.')
  #print(sys.argv, len(sys.argv))
  code = sys.argv[1] if len(sys.argv)>1 else ''
  if code!='':
    d = treipreter(code)
    d.save_png('tmp.png')
