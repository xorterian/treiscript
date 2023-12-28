## Init function making simple addition, multiplication and composition
## Scope can be displayed if the precedence is not defined or confusing
## Should be extended with further ops and make it multivariable
## Substraction and division are defined by addition and multiplication with inversion at the second operand.

# Ops / add{A}{B}
def add(A,B,scope=False):
  dim_A = (A.width, A.height)
  dim_B = (B.width, B.height)
  d = draw.Drawing(dim_A[0]+dx+dim_B[0],max(dim_A[1],dim_B[1]) + (dx/2 if scope else 0))
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  for e in copy.deepcopy(B.all_elements()):
    group_B.append(e)
  group_Op = draw.Group()
  if scope:
    group_Op.append(draw.Line(dim_A[0]+dx/2,0,dim_A[0]+dx/2,d.height-dx/4, stroke='black', stroke_width=str(dx/6)))
    group_Op.append(draw.Line(0,d.height-dx/4,d.width,d.height-dx/4,stroke='black', stroke_width=str(dx/6)))
  else:
    group_Op.append(draw.Line(dx/2,0,dx/2,d.height, stroke='black', stroke_width=str(dx/6)))
  offset_y_2B = B.height-A.height if A.height < B.height else 0
  offset_y_2A = A.height-B.height if A.height > B.height else 0
  d.append(draw.Use(group_A,0,offset_y_2B))
  d.append(draw.Use(group_Op,0 if scope else dim_A[0],0))
  d.append(draw.Use(group_B,dim_A[0]+dx,offset_y_2A))
  return d

def mul(A,B,scope=False):
  dim_A = (A.width, A.height)
  dim_B = (B.width, B.height)
  d = draw.Drawing(dim_A[0]+dx+dim_B[0],max(dim_A[1],dim_B[1]) + (dx/2 if scope else 0))
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  for e in copy.deepcopy(B.all_elements()):
    group_B.append(e)
  group_Op = draw.Group()
  if scope:
    group_Op.append(draw.Line(dim_A[0]+dx/2-dx/6,0,dim_A[0]+dx/2-dx/6,d.height-dx/4, stroke='black', stroke_width=str(dx/6)))
    group_Op.append(draw.Line(dim_A[0]+dx/2+dx/6,0,dim_A[0]+dx/2+dx/6,d.height-dx/4, stroke='black', stroke_width=str(dx/6)))
    group_Op.append(draw.Line(0,d.height-dx/4,d.width,d.height-dx/4,stroke='black', stroke_width=str(dx/6)))
  else:
    group_Op.append(draw.Line(dx/2-dx/6,0,dx/2-dx/6,d.height, stroke='black', stroke_width=str(dx/6)))
    group_Op.append(draw.Line(dx/2+dx/6,0,dx/2+dx/6,d.height, stroke='black', stroke_width=str(dx/6)))
  offset_y_2B = B.height-A.height if A.height < B.height else 0
  offset_y_2A = A.height-B.height if A.height > B.height else 0
  d.append(draw.Use(group_A,0,offset_y_2B))
  d.append(draw.Use(group_Op,0 if scope else dim_A[0],0))
  d.append(draw.Use(group_B,dim_A[0]+dx,offset_y_2A))
  return d

# Ops / comp{A}{B}
def comp(A,B,scope=False):
  dim_A = (A.width, A.height)
  dim_B = (B.width, B.height)
  d = draw.Drawing(dim_A[0]+dx+dim_B[0],max(dim_A[1],dim_B[1]) + (dx/2 if scope else 0))
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_B = draw.Group()
  for e in copy.deepcopy(B.all_elements()):
    group_B.append(e)
  group_Op = draw.Group()
  if scope:
    group_Op.append(draw.Circle(dim_A[0]+dx/2,d.height/2-dx/3,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
    group_Op.append(draw.Line(dim_A[0]+dx/2,d.height/2-dx/6,dim_A[0]+dx/2,d.height-dx/4, stroke='black', stroke_width=str(dx/6)))
    group_Op.append(draw.Line(0,d.height-dx/4,d.width,d.height-dx/4,stroke='black', stroke_width=str(dx/6)))
  else:
    group_Op.append(draw.Circle(dx/2,d.height/2,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
  offset_y_2B = B.height-A.height if A.height < B.height else 0
  offset_y_2A = A.height-B.height if A.height > B.height else 0
  d.append(draw.Use(group_A,0,offset_y_2B))
  d.append(draw.Use(group_Op,0 if scope else dim_A[0],0))
  d.append(draw.Use(group_B,dim_A[0]+dx,offset_y_2A))
  return d
