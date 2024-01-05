## Init and test formulas

from matplotlib import mathtext, font_manager
import matplotlib as mpl
mpl.rcParams['savefig.transparent'] = True
texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')

!pip install "drawsvg~=2.0"
!pip install "cairosvg"

import drawsvg as draw
import copy

dx = 32

import init-symbols-vars-and-cons
import init-index
import init-basic-ops
import init-invs-and-unaries
import init-sets
import init-basic-rels-and-logics
import numeriz
import pow
import correspondence
import bigop

## Sample II.
# Derivative
A = pow(d_var_f,'',typ='D')
R = d_rel_eq
B = mul(add(comp(d_var_f,add(d_var_x,d_var_dx),True),inv_add(comp(d_var_f,d_var_x,True))), inv_mul(d_var_dx),True)
padding = dx/7
d = make_rel(A,R,B)
d.save_png('tmp.png')

if __name__=='__main__':
  print('Packages are processed.')
