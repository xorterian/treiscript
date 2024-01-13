# Import each engine-related module
import drawsvg as draw
import copy
from __main__ import dx

from visu import *

folder = 'core.'
for to_import in ['treipreter']:
  exec('from '+folder+to_import+' import *')
