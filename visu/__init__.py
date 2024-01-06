# Import each visualization-related module
# Try not to look at it
import drawsvg as draw
import copy
from __main__ import dx

folder = 'visu.'
for to_import in ['init_symbols_vars_and_cons', 'init_index', 'init_basic_ops', 'init_invs_and_unaries', 'init_sets', 'init_basic_rels_and_logics', 'numeriz', 'pow', 'correspondence', 'bigop']:
  exec('from '+folder+to_import+' import *')
