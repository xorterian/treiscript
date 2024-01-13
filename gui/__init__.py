# Import each graphics-related module
import drawsvg as draw
import copy
from __main__ import dx

folder = 'gui.'
for to_import in ['viewer']:
  exec('from '+folder+to_import+' import *')
