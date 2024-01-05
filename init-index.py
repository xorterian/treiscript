# Indexing
# Make a variable indexed

def index_var(A='x',index='\'',pos=''):
  # A: variable (as a string)
  # index of the variable like integers, primes or other expressions
  # pos: up/down, smooth/- only at non-string variables
  corner='top'
  if isinstance(A,str):
    if A=='x':
      A = d_var_x
    elif A=='y':
      A = d_var_y
      corner='bottom'
    elif A=='f':
      A = d_var_f
    elif A=='g':
      A = d_var_g
      corner='bottom'
    elif A=='dx':
      A = d_var_dx
    elif A=='dy':
      A = d_var_dy
      corner='bottom'
    elif A=='O':
      A = d_var_O
    elif A=='P':
      A = d_var_P
      corner='bottom'
    elif A=='M':
      A = d_var_M
    elif A=='N':
      A = d_var_N
      corner='bottom'
    else:
      A = d_var_x
  else:
    corner='top_edge'
  isInner = False
  if isinstance(index,str):
    if index=='\'':
      index = draw.Drawing(dx/6,dx/3)
      index.append(draw.Line(dx/12,0,dx/12,dx/3,stroke='black', stroke_width=str(dx/10)))
    elif index=='\'\'':
      index = draw.Drawing(dx/6*2,dx/3)
      index.append(draw.Line(dx/12,0,dx/12,dx/3,stroke='black', stroke_width=str(dx/10)))
      index.append(draw.Line(dx/6 + dx/12,0,dx/6 + dx/12,dx/3,stroke='black', stroke_width=str(dx/10)))
    elif index=='\'\'\'':
      index = draw.Drawing(dx/6*3,dx/3)
      index.append(draw.Line(dx/12,0,dx/12,dx/3,stroke='black', stroke_width=str(dx/10)))
      index.append(draw.Line(dx/6 + dx/12,0,dx/6 + dx/12,dx/3,stroke='black', stroke_width=str(dx/10)))
      index.append(draw.Line(dx/6*2 + dx/12,0,dx/6*2 + dx/12,dx/3,stroke='black', stroke_width=str(dx/10)))
    elif -15<=int(index)<=15:
      index = numeriz(int(index))
  elif isinstance(index,int):
    index = numeriz(int(index))
  else:
    isInner = True
  group_A = draw.Group()
  for e in copy.deepcopy(A.all_elements()):
    group_A.append(e)
  group_I = draw.Group()
  for e in copy.deepcopy(index.all_elements()):
    group_I.append(e)
  if corner=='top':
    if index.height==dx/3:
      d = draw.Drawing(A.width + index.width - dx/6, A.height)
      d.append(draw.Use(group_A,0,0))
      d.append(draw.Use(group_I,A.width - dx/3,0))
    else:
      d = draw.Drawing(A.width + index.width - dx/3 + (dx+dx*2/3 if isInner else 0), A.height + index.height+dx/6)
      d.append(draw.Use(group_A,0,index.height+dx/6))
      d.append(draw.Circle(A.width,index.height+dx/6+dx/6,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
      if not isInner:
        d.append(draw.Use(group_I,A.width - index.width + dx*2/3,0))
        d.append(draw.Line(A.width + dx*3/5 - index.width/2,index.height+dx/6,A.width + dx*3/5 - index.width/2,index.height-dx*2/5, stroke='black', stroke_width=str(dx/8)))
      else:
        d.append(draw.Line(A.width,index.height+dx/6,A.width,index.height/2, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width,index.height/2,A.width +dx/2,index.height/2, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width +dx/2,index.height,A.width +dx/2,0, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width +dx/2,index.height,A.width +dx/2+dx/4,index.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width +dx/2,0,A.width +dx/2+dx/4,0, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Use(group_I,A.width + dx*2/3 + dx/12,0))
        d.append(draw.Line(A.width + index.width +dx,index.height,A.width + index.width + dx,0, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width + index.width +dx,index.height,A.width + index.width + dx - dx/4,index.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width + index.width +dx,0,A.width + index.width + dx - dx/4,0, stroke='black', stroke_width=str(dx/8)))
  elif corner=='bottom':
    if index.height==dx/3:
      d = draw.Drawing(A.width + index.width, A.height)
      d.append(draw.Use(group_A,0,0))
      d.append(draw.Use(group_I,A.width,0))
    else:
      d = draw.Drawing(A.width + index.width - dx/3 + (dx+dx*2/3 if isInner else 0), A.height + index.height+dx/6)
      d.append(draw.Use(group_A,0,0))
      d.append(draw.Circle(A.width,A.height-dx/6,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
      if not isInner:
        d.append(draw.Use(group_I,A.width - index.width + dx*2/3,A.height))
        d.append(draw.Line(A.width + dx*3/5 - index.width/2,A.height,A.width + dx*3/5 - index.width/2,A.height+dx*2/5, stroke='black', stroke_width=str(dx/8)))
      else:
        d.append(draw.Line(A.width,A.height,A.width,A.height+index.height/2, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width,A.height+index.height/2,A.width +dx/2,A.height+index.height/2, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width +dx/2,A.height+index.height,A.width +dx/2,A.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width +dx/2,A.height+index.height,A.width +dx/2+dx/4,A.height+index.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width +dx/2,A.height,A.width +dx/2+dx/4,A.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Use(group_I,A.width + dx*2/3 + dx/12,A.height))
        d.append(draw.Line(A.width + index.width +dx,A.height+index.height,A.width + index.width + dx,A.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width + index.width +dx,A.height+index.height,A.width + index.width + dx - dx/4,A.height+index.height, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(A.width + index.width +dx,A.height,A.width + index.width + dx - dx/4,A.height, stroke='black', stroke_width=str(dx/8)))
  else: # on edge
    if 'down' in pos:
      corner = 'bottom'
    else:
      corner = 'top'
    d = draw.Drawing(A.width+index.width+dx*5/2, A.height+index.height+dx/2)
    if corner=='top':
      dJ = index.height + dx/2
      d.append(draw.Use(group_A,dx/4,dJ))
      d.append(draw.Line(0,dJ,0,dJ+A.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(A.width+dx/2,dJ,A.width+dx/2,dJ+A.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(0,dJ,dx/4,dJ, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(0,dJ+A.height,dx/4,dJ+A.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(A.width+dx/2,dJ,A.width+dx/4,dJ, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(A.width+dx/2,dJ+A.height,A.width+dx/4,dJ+A.height, stroke='black', stroke_width=str(dx/8)))

      dL, dJ = A.width+dx*3/2, 0
      d.append(draw.Use(group_I,dL+dx/2,dJ))
      d.append(draw.Line(dL,dJ,dL,dJ+index.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL+index.width+dx,dJ,dL+index.width+dx,dJ+index.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL,dJ,dL+dx/4,dJ, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL,dJ+index.height,dL+dx/4,dJ+index.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL+index.width+dx,dJ,dL+index.width+dx-dx/4,dJ, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL+index.width+dx,dJ+index.height,dL+index.width+dx-dx/4,dJ+index.height, stroke='black', stroke_width=str(dx/8)))

      dJ = index.height
      if 'smooth' in pos:
        d.append(draw.Line(dL-dx,dJ+dx/2,dL,dJ, stroke='black', stroke_width=str(dx/8)))
      else:
        d.append(draw.Circle(dL-dx/2,dJ+dx/2,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(dL-dx/2,dJ+dx/2-dx/6,dL-dx/2,index.height/2, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(dL-dx/2,index.height/2,dL,index.height/2, stroke='black', stroke_width=str(dx/8)))

    else: # bottom
      d.append(draw.Use(group_A,dx/4,0))
      d.append(draw.Line(0,0,0,A.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(A.width+dx/2,0,A.width+dx/2,A.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(0,0,dx/4,0, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(0,A.height,dx/4,A.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(A.width+dx/2,0,A.width+dx/4,0, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(A.width+dx/2,A.height,A.width+dx/4,A.height, stroke='black', stroke_width=str(dx/8)))

      dL, dJ = A.width+dx*3/2, A.height+dx/2
      d.append(draw.Use(group_I,dL+dx/2,dJ))
      d.append(draw.Line(dL,dJ,dL,dJ+index.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL+index.width+dx,dJ,dL+index.width+dx,dJ+index.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL,dJ,dL+dx/4,dJ, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL,dJ+index.height,dL+dx/4,dJ+index.height, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL+index.width+dx,dJ,dL+index.width+dx-dx/4,dJ, stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(dL+index.width+dx,dJ+index.height,dL+index.width+dx-dx/4,dJ+index.height, stroke='black', stroke_width=str(dx/8)))

      if 'smooth' in pos:
        d.append(draw.Line(dL-dx,dJ-dx/2,dL,dJ, stroke='black', stroke_width=str(dx/8)))
      else:
        d.append(draw.Circle(dL-dx/2,dJ-dx/2,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(dL-dx/2,dJ-dx/2+dx/6,dL-dx/2,dJ+index.height/2, stroke='black', stroke_width=str(dx/8)))
        d.append(draw.Line(dL-dx/2,dJ+index.height/2,dL,dJ+index.height/2, stroke='black', stroke_width=str(dx/8)))
        
  return d
