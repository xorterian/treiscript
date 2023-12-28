## Init functions making something inverted in addition, multiplication, function.
## Init functions making something a set or a vector [need to update!]

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

def make_set(A):
  dim = (A.width, A.height)
  d = draw.Drawing(dim[0]+dx/3,dim[1]+2*dx/3)
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  group_B.append(draw.Line(0,dx/3,dim[0]+dx/3,dx/3, stroke='black', stroke_width=str(dx/8)))
  group_B.append(draw.Line(0,dx/3,0,1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
  group_B.append(draw.Line(dim[0]+dx/3,dx/3,dim[0]+dx/3,1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
  d.append(draw.Use(group_A,dx/6,2*dx/3))
  d.append(draw.Use(group_B,0,0))
  return d

def make_vec(A):
  dim = (A.width, A.height)
  d = draw.Drawing(dim[0]+dx/3,dim[1]+2*dx/3)
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  group_B.append(draw.Line(0,dx/3,dim[0]+dx/3,dx/3, stroke='black', stroke_width=str(dx/8)))
  group_B.append(draw.Line(0,dx/3,0,dx/3-1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
  group_B.append(draw.Line(dim[0]+dx/3,dx/3,dim[0]+dx/3,dx/3-1.8*dx/3, stroke='black', stroke_width=str(dx/8)))
  d.append(draw.Use(group_A,dx/6,2*dx/3))
  d.append(draw.Use(group_B,0,0))
  return d
