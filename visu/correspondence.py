## It is useful to understand a mathematical object via its inner correspondences
## For example a single variable function can be R -> R
## A functional like definite integral or big operator productum can be (R -> R) -> R
## An operator like derivative can be (R -> R) -> (R -> R)
## And so on, you can define any kind of higher correspondence generally named metarators in TreiScript.

from . import *

# Ops / cor (correspondence: f : x -> y)
def cor(A='',B='', typA='func', typB='none'):
  if A=='' and B=='':
    d = draw.Drawing(dx/2,dx)
    d_p1 = draw.Circle(dx/4,dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
    d_p2 = draw.Circle(dx/4,3*dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
    d_x = draw.Line(dx/4,dx/4+dx/8,dx/4,3*dx/4-dx/8, stroke='black', stroke_width=str(dx/8))
    d.append(d_p1)
    d.append(d_p2)
    d.append(d_x)
    return d

  dim_A = (A.width, A.height)
  dim_B = (B.width, B.height)
  pad_y = dx/2
  pad_x_A, pad_x_B = 0, 0
  typB = typA if typB=='none' else typB
  if typA=='func':
    pad_x_A = dx/5
  elif typA=='cor':
    pad_x_A = -dx/4
  if typB=='func':
    pad_x_B = dx/5
  elif typB=='cor':
    pad_x_B = -dx/4
  d = draw.Drawing(dx + max(dim_A[0],dim_B[0]), pad_y + dim_A[1]+dim_B[1])
  group_A = draw.Group()
  for e in copy.deepcopy(A).all_elements():
    group_A.append(e)
  group_B = draw.Group()
  for e in copy.deepcopy(B).all_elements():
    group_B.append(e)
  d_p1 = draw.Circle(dx/4,dim_A[1]/2,dx/6, stroke='black', stroke_width=str(dx/8))
  d_p2 = draw.Circle(dx/4,dim_A[1]+pad_y+dim_B[1]/2,dx/6, stroke='black', stroke_width=str(dx/8))
  d_x = draw.Line(dx/4,dim_A[1]/2+dx/8,dx/4,dim_A[1]+pad_y+dim_B[1]/2-dx/8, stroke='black', stroke_width=str(dx/8))
  d_p1_2_A = draw.Line(dx/4+dx/8,dim_A[1]/2,dx-pad_x_A,dim_A[1]/2, stroke='black', stroke_width=str(dx/8))
  d_p2_2_B = draw.Line(dx/4+dx/8,dim_A[1]+pad_y+dim_B[1]/2,dx-pad_x_B,dim_A[1]+pad_y+dim_B[1]/2, stroke='black', stroke_width=str(dx/8))
  d.append(d_p1)
  d.append(d_p2)
  d.append(d_x)
  d.append(d_p1_2_A)
  d.append(d_p2_2_B)
  d.append(draw.Use(group_A,dx,0))
  d.append(draw.Use(group_B,dx,dim_A[1]+pad_y))
  return d
