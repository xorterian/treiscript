## Init functions making something inverted in addition, multiplication, function.
## Init functions making something a set or a vector [need to update!]

from . import *

# Ops / inv_add{1}
A = d_cons_15
def inv_add(A):
  dim = (A.width, A.height)
  d = draw.Drawing(dim[0],dim[1]+dx/6)
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  group_B.append(draw.Line(0,0,dim[0],0, stroke='black', stroke_width=str(dx/8)))
  d.append(draw.Use(group_A,0,dx/6))
  d.append(draw.Use(group_B,0,0))
  return d

# Ops / inv_mul{1}
A = d_cons_15
def inv_mul(A):
  dim = (A.width, A.height)
  d = draw.Drawing(dim[0],dim[1]+2*dx/5)
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  group_B.append(draw.Rectangle(0,0,dim[0],dx/4, stroke='black', fill='none', stroke_width=str(dx/8)))
  d.append(draw.Use(group_A,0,2*dx/5))
  d.append(draw.Use(group_B,0,0))
  return d

# Ops / inv_fun{1}
A = d_var_y
def inv_fun(A):
  dim = (A.width, A.height)
  d = draw.Drawing(dim[0]+dx/6,dim[1]+2*dx/3)
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  group_B.append(draw.Line(0,dx/3,dim[0]-dx/6,dx/3, stroke='black', stroke_width=str(dx/8)))
  group_B.append(draw.Circle(dim[0],dx/3,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
  d.append(draw.Use(group_A,0,2*dx/3))
  d.append(draw.Use(group_B,0,0))
  return d

def make_set(A,card='',depth='',isPower=False, isDisordered=True):
  # Make a set/vector from an expression A
  # You can give the cardinality of the set
  # You can give embedness/nestedness of the set like {{{x}}}
  # Given cardinality can be used rather as power exponent of the set: R×R×...×R
  # You can distuing between vector and set by switching ordering truth value
  earlet = 1.8*dx/3 if isDisordered else dx/3 - 1.8*dx/3
  dim = (A.width, A.height)
  if card=='' and depth=='':
    d = draw.Drawing(dim[0]+dx/3,dim[1]+2*dx/3)
    group_A = draw.Group()
    for e in copy.deepcopy(A.all_elements()):
      group_A.append(e)
    group_B = draw.Group()
    group_B.append(draw.Line(0,dx/3,dim[0]+dx/3,dx/3, stroke='black', stroke_width=str(dx/8)))
    group_B.append(draw.Line(0,dx/3,0,earlet, stroke='black', stroke_width=str(dx/8)))
    group_B.append(draw.Line(dim[0]+dx/3,dx/3,dim[0]+dx/3,earlet, stroke='black', stroke_width=str(dx/8)))
    d.append(draw.Use(group_A,dx/6,2*dx/3))
    d.append(draw.Use(group_B,0,0))
  else:
    if isinstance(card,str):
      if card=='':
        card = draw.Drawing(0,0)
        isPower = False
      else:
        card = numeriz(int(card)) if 0<=int(card)<16 else draw.Drawing(0,0)
    if isinstance(depth,str):
      if depth=='':
        depth = draw.Drawing(0,0)
      else:
        depth = numeriz(int(depth)) if 0<=int(depth)<16 else draw.Drawing(0,0)
    dim_card = (card.width, card.height)
    dim_depth = (depth.width, depth.height)
    extra_y = max(dim_depth[1]/2,dim_card[1]) if dim_card[0]>0 else dim_depth[1]/2-dx/3
    d = draw.Drawing(dim[0]+dx/3 + dx + dim_depth[0],dim[1]+2*dx/3 + extra_y)
    group_A = draw.Group()
    for e in copy.deepcopy(A.all_elements()):
      group_A.append(e)
    group_card = draw.Group()
    for e in copy.deepcopy(card.all_elements()):
      group_card.append(e)
    group_depth = draw.Group()
    for e in copy.deepcopy(depth.all_elements()):
      group_depth.append(e)
    group_B = draw.Group()
    if dim_depth[0]==0:
      group_B.append(draw.Line(0,dx/3,dim[0]+dx/3,dx/3, stroke='black', stroke_width=str(dx/8)))
      group_B.append(draw.Line(0,dx/3,0,earlet, stroke='black', stroke_width=str(dx/8)))
      group_B.append(draw.Line(dim[0]+dx/3,dx/3,dim[0]+dx/3,earlet, stroke='black', stroke_width=str(dx/8)))
    else:
      group_B.append(draw.Line(0,dx/3,dim[0]+dx/2,dx/3, stroke='black', stroke_width=str(dx/8)))
      if isDisordered:
        group_B.append(draw.Line(dim[0]+1.8*dx/3,dx/3+dx/6,dim[0]+1.8*dx/3,dx/3+dx/6+1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
        group_B.append(draw.Line(0,dx/3,0,dx/3+dx/6+earlet, stroke='black', stroke_width=str(dx/8)))
      else:
        group_B.append(draw.Line(dim[0]+1.8*dx/3,dx/3-dx/6,dim[0]+1.8*dx/3,dx/3-dx/6-1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
        group_B.append(draw.Line(0,dx/3,0,dx/3-dx/6-1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
      group_B.append(draw.Circle(dim[0]+1.8*dx/3,dx/3,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
      group_B.append(draw.Line(dim[0]+1.8*dx/3+dx/6,dx/3,dim[0]+1.8*dx/3-dx/6+dx,dx/3, stroke='black', stroke_width=str(dx/8)))
    if isPower:
      group_B.append(draw.Line(2*dx/3 - dim_card[0]/2 + dim[0]/2,0,2*dx/3 - dim_card[0]/2 + dim[0]/2,dx/3, stroke='black', stroke_width=str(dx/8)))
    d.append(draw.Use(group_A,dx/6,2*dx/3 + extra_y))
    d.append(draw.Use(group_B,0,extra_y))
    d.append(draw.Use(group_card,dx/6 + dim[0]/2-dim_card[0]/2,0))
    d.append(draw.Use(group_depth,dim[0] + dx/3 + dx,extra_y + dx/3 - dim_depth[1]/2))
  return d

def make_vec(A,size_A='',depth='',isPower=False, isDisordered=False):
  return make_set(A,card=size_A,depth=depth,isPower=isPower, isDisordered=isDisordered)
