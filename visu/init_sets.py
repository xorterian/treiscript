## Init basic sets like reals and integers
## Init function notating something is in a set

from . import *

# Sets / R
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Circle(dx/2,dx/2,dx/7, stroke='black', stroke_width='1'))
d_set_R = d

# Sets / Z
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Circle(dx/2,dx/2,dx/6, stroke='black', fill='none', stroke_width=str(dx/12)))
d_set_Z = d

# Sets / Rp
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.725*dx,dx/2,dx/7, stroke='black', stroke_width='1'))
d_set_Rp = d

# Sets / Rm
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.275*dx,dx/2,dx/7, stroke='black', stroke_width='1'))
d_set_Rm = d

# Sets / Zp
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.8*dx,dx/2,dx/6, stroke='black', fill='none', stroke_width=str(dx/12)))
d_set_Zp = d

# Sets / Zm
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.2*dx,dx/2,dx/6, stroke='black', fill='none', stroke_width=str(dx/12)))
d_set_Zm = d

# Sets / Rp U {0}
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.725*dx,dx/2,dx/7, stroke='black', stroke_width='1'))
d.append(draw.Line(dx/2,dx/2,.725*dx-dx/7,dx/2, stroke='black', stroke_width=str(dx/8)))
d_set_Rp0 = d

# Sets / Rm U {0}
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.275*dx,dx/2,dx/7, stroke='black', stroke_width='1'))
d.append(draw.Line(dx/2,dx/2,.275*dx+dx/7,dx/2, stroke='black', stroke_width=str(dx/8)))
d_set_Rm0 = d

# Sets / Zp U {0} = N
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.8*dx,dx/2,dx/6, stroke='black', fill='none', stroke_width=str(dx/12)))
d.append(draw.Line(dx/2,dx/2,.8*dx-dx/6,dx/2, stroke='black', stroke_width=str(dx/8)))
d_set_Zp0 = d

# Sets / Zm U {0}
d = draw.Drawing(dx,dx)
d.append(draw.Circle(dx/2,dx/2,dx/2, stroke='black', fill='none', stroke_width=str(dx/8)))
d.append(draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8)))
d.append(draw.Circle(.2*dx,dx/2,dx/6, stroke='black', fill='none', stroke_width=str(dx/12)))
d.append(draw.Line(dx/2,dx/2,.2*dx+dx/6,dx/2, stroke='black', stroke_width=str(dx/8)))
d_set_Zm0 = d

# Ops / set_in{A}{B}
def set_in(A,B):
  nomenic = False
  if isinstance(B,str):
    B = B.lower() \
    .replace('positive','+').replace('pos','+') \
    .replace('negative','-').replace('neg','-') \
    .replace('zero','0').replace('null','0').replace('nul','0') \
    .replace('real','r').replace('whole','z') \
    .replace('integer','z').replace('int','z') \
    .replace('rational','q').replace('rat','q').replace('fraction','q')
    if B == 'r':
      B = d_set_R
    elif B == 'r+':
      B = d_set_Rp
    elif B == 'r-':
      B = d_set_Rm
    elif B == 'r+0':
      B = d_set_Rp0
    elif B == 'r-0':
      B = d_set_Rm0
    if B == 'z':
      B = d_set_Z
    elif B == 'z+':
      B = d_set_Zp
    elif B == 'z-':
      B = d_set_Zm
    elif B == 'z+0':
      B = d_set_Zp0
    elif B == 'z-0':
      B = d_set_Zm0
    nomenic = True

  dim_A = (A.width, A.height)
  dim_B = (B.width, B.height)
  if not nomenic:
    d = draw.Drawing(dim_A[0]+dx+dim_B[1]/2+dim_B[0],max(dim_A[1],dim_B[1]))
    group_A = draw.Group()
    for e in copy.deepcopy(A.all_elements()):
      group_A.append(e)
    group_B = draw.Group()
    for e in copy.deepcopy(B.all_elements()):
      group_B.append(e)
    group_Op = draw.Group()
    group_Op.append(draw.Line(0,dx/2,3*dx/4,dx/2, stroke='black', stroke_width=str(dx/8)))
    group_Op.append(draw.Arc(3*dx/4+dim_B[1]/2,dx/2,dim_B[1]/2,270,90, stroke='black', fill='none', stroke_width=str(dx/8)))
  else:
    d = draw.Drawing(dim_A[0]+dx+dim_B[0],max(dim_A[1],dim_B[1]))
    group_A = draw.Group()
    for e in copy.deepcopy(A.all_elements()):
      group_A.append(e)
    group_B = draw.Group()
    for e in copy.deepcopy(B.all_elements()):
      group_B.append(e)
    group_Op = draw.Group()
    group_Op.append(draw.Line(dx/4,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8)))

  offset_y_2B = (B.height-A.height)/2 if A.height < B.height else 0
  offset_y_2A = (A.height-B.height)/2 if A.height > B.height else 0
  d.append(draw.Use(group_A,0,offset_y_2B))
  d.append(draw.Use(group_Op,dim_A[0],offset_y_2B+offset_y_2A))
  d.append(draw.Use(group_B,dim_A[0]+dx+(0 if nomenic else dim_B[1]/2),offset_y_2A))

  return d
