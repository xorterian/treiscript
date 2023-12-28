## Define general power-notation
## In powers you have a base and one or more exponents
## Each exponents has a type and level
## The simplest case is the well-known exponentiation whose level is 3 and the type is not notated
## At levels 1 and 2 we are talking about addition and multiplication while at levels 4 and above it is tetration and higher hyperoperators
## The type 'o' leads functional power that is iterated function-composition: f o f o ... o f
## The type 'D' leads n-th derivative, the type '->' is of correspondence and so on.
## A power can displayed in floating and non-floating mode depending on the will to have it higher or longer.
## To-do:
### - fix padding issues
### - extend with more types
### - do the same in inverses of left (logarithm) and right (root)

# Ops / pow{x}{y}{typ=''}{n=3}{floating=True}
def pow(x,y, typ='', n='', floating=True):
  if x in ['e', 'E', '', math.exp(1)]:
    x = draw.Drawing(dx/4,dx/2) # If natural base, then it is not displayed,
    floating=True # and it must be floating.
  if not isinstance(y, list):
    y = [y]
  if not isinstance(typ, list):
    typ = [ typ for _ in y ]
  if not isinstance(n, list):
    n = [ n for _ in y ]
  y = [ (e if e!='' else draw.Drawing(0,dx*7/8)) for e in y ]
  typ = [ (e if e!='' else draw.Drawing(0,dx*7/8)) for e in typ ]

  dim_x = (x.width, x.height)
  dim_Y = [ (ys.width, ys.height) for ys in y ]
  d_width = dx/3 + dim_x[0] #+ 3*dx/5 + (0 if floating else dx/3)
  d_height = dim_x[1] - dx/3 - (dim_x[1]/3 if floating else 0)
  if floating:
    d_width += + max([ ys.width for ys in y ]) + dx*(3/6+2)
    d_height += sum([ ys.height for ys in y ]) + len(y)*dx/3 #o.k.
    d_width -=  dx
  else:
    d_width += sum([ ys.width for ys in y ]) + len(y)*dx*(5/6+2) #o.k.
    d_height = max([d_height]+[ ys.height for ys in y ]) + dx/3 #o.k.
    d_width -=  len(y)*dx

  d = draw.Drawing(d_width, d_height)
  group_x = draw.Group()
  for e in copy.deepcopy(x).all_elements():
    group_x.append(e)
  group_Y = [ draw.Group() for _ in y ]
  for i in range(len(y)):
    for e in copy.deepcopy(y[i]).all_elements():
      group_Y[i].append(e)
  group_pow = draw.Group()

  pos_x = (dx/3,d_height-dim_x[1])
  L = dx/6 # current horizontal position
  J = pos_x[1] + dim_x[1]/3 # current vertical position
  d.append(draw.Line(L,J,L,J-dim_x[1]/3-dx/6,stroke='black', stroke_width=str(dx/8)))
  J -= dim_x[1]/3+dx/6
  pos_Typ = []
  pos_N = []
  pos_Y = []
  if floating:
    L0 = L
    Jprev = J
    for i in range(len(y)):
      L = L0
      if i>0:
        J = Jprev-dim_Y[i-1][1]/2-dx/3-dim_Y[i][1]/2
        d.append(draw.Line(L,Jprev,L,J,stroke='black', stroke_width=str(dx/8)))
      Jprev = J
      d.append(draw.Line(L,J,L+dim_x[0]+dx/3,J,stroke='black', stroke_width=str(dx/8)))
      L += dim_x[0]+ dx/3
      pos_Typ.append((L, J-dx/2) if typ[i]!='' else 0)
      L += dx
      if isinstance(n[i],int):
        if 0 <= n[i] and n[i] <= 15: # If n is a simple integer under 16.
          pos_N.append((L, J-dx/2))
          L += dx
      elif n[i]!='': # If n is other symbol:
        pos_N.append((L, J-n[i].height/2))
        L += n[i].width + dx/2
      pos_Y.append((L, J-dim_Y[i][1]/2))
  else: # not floating
    d.append(draw.Line(L,J,L+dim_x[0]+dx/3,J,stroke='black', stroke_width=str(dx/8)))
    L += dim_x[0]+dx/3
    d.append(draw.Line(L,J,L,dx/6,stroke='black', stroke_width=str(dx/8)))
    J = dx/6
    J0 = J
    Lprev = L
    for i in range(len(y)):
      J = J0
      if i>0:
        if d_height-J<dim_Y[i-1][1]:
          d.append(draw.Line(Lprev,J,Lprev,J-dim_Y[i-1][1],stroke='black', stroke_width=str(dx/8)))
          J -= dim_Y[i-1][1]
        L += dim_Y[i-1][0] + dx/3
      d.append(draw.Line(Lprev,J,L,J,stroke='black', stroke_width=str(dx/8)))
      d.append(draw.Line(L,J,L+2*dx/6,J,stroke='black', stroke_width=str(dx/8)))
      L += dx/6*2
      d.append(draw.Line(L,J,L,d.height-dx/2,stroke='black', stroke_width=str(dx/8)))
      J = d.height-dx/2
      d.append(draw.Line(L,J,L+dx/6,J,stroke='black', stroke_width=str(dx/8)))
      L += dx/6
      pos_Typ.append((L, J-dx/2) if typ[i]!='' else 0)
      L += dx
      if isinstance(n[i],int):
        if 0 <= n[i] and n[i] <= 15: # If n is a simple integer under 16.
          pos_N.append((L, J-dx/2))
          L += dx
      elif n[i]!='': # If n is other symbol:
        pos_N.appned((L, J-n[i].height/2))
        L += n[i].width + dx/2
      #pos_Y.append((L, d.height-J-dim_Y[i][1]/2+dx/3)) # ?
      pos_Y.append((L, d.height-dim_Y[i][1])) # ?
  for i in range(len(y)):
    if dim_Y[i][1]/2 > dim_x[1] + dx/6:
      pos_Y[i] = (pos_Y[i][0], 0)
    pos_Y[i] = (pos_Y[i][0]+dx/5, pos_Y[i][1])

  # Draw types:
  group_Typ = []
  for i in range(len(y)):
    if typ[i]!='':
      group_typ = draw.Group()
      if typ[i] in ['func', 'fun', 'functional', 'o']:
        group_typ.append(draw.Line(0,dx/2,dx/2-dx/6,dx/2,stroke='black', stroke_width=str(dx/8)))
        group_typ.append(draw.Circle(dx/2,dx/2,dx/6, fill="none", stroke='black', stroke_width=str(dx/8)))
        if n[i]!='':
          group_typ.append(draw.Line(dx/2+dx/6,dx/2,dx,dx/2,stroke='black', stroke_width=str(dx/8)))

      elif typ[i] in ['cor', 'corres', 'correspondence', '->']:
        group_typ.append(draw.Line(0,dx/2,dx/2 if n[i]=='' else dx,dx/2,stroke='black', stroke_width=str(dx/8)))
        group_typ.append(draw.Circle(dx/2,dx/2-dx/3,dx/8, stroke='black', stroke_width=str(dx/8)))
        group_typ.append(draw.Circle(dx/2,dx/2+dx/3,dx/8, stroke='black', stroke_width=str(dx/8)))
        group_typ.append(draw.Line(dx/2,dx/2+dx/6-dx/3,dx/2,dx/2+dx/6+dx/3, stroke='black', stroke_width=str(dx/8)))

      elif typ[i] in ['der', 'D', 'derivative', '^']:
        group_typ.append(draw.Line(0,dx/2,dx*2/5,dx/2,stroke='black', stroke_width=str(dx/8)))
        group_typ.append(draw.Line(dx/4,dx*2/3,dx/2,dx/3,stroke='black', stroke_width=str(dx/8)))
        group_typ.append(draw.Line(dx/2,dx/3,dx*3/4,dx*2/3,stroke='black', stroke_width=str(dx/8)))
        if n[i]!='':
          group_typ.append(draw.Line(dx*3/5,dx/2,dx,dx/2,stroke='black', stroke_width=str(dx/8)))

      else: # Default line.
        group_typ.append(draw.Line(0,dx/2,dx/2 if n[i]=='' else dx,dx/2,stroke='black', stroke_width=str(dx/8)))

    group_Typ.append(group_typ)

  # Draw iteration level n:
  group_N = []
  for i in range(len(y)):
    group_n = draw.Group()
    if n[i]!='':
      #group_n = draw.Group()
      if n[i]==round(n[i]) and 0 <= n[i] and n[i] <= 15:
        group_n.append(draw.Line(0,dx/2,2*dx/5,dx/2,stroke='black', stroke_width=str(dx/8)))
        for e in copy.deepcopy(eval('d_cons_' + str(n[i]) + '.all_elements()')):
          group_n.append(e)
      else:
        pass
    group_N.append(group_n)

  # Copy x, y, typ and n to its places
  d.append(draw.Use(group_x,pos_x[0],pos_x[1]))
  for i in range(len(y)):
    d.append(draw.Use(group_Y[i],pos_Y[i][0],pos_Y[i][1]))
    if typ[i]!='':
      d.append(draw.Use(group_Typ[i],pos_Typ[i][0],pos_Typ[i][1]))
    if n[i]!='':
      d.append(draw.Use(group_N[i],pos_N[i][0],pos_N[i][1]))

  return d
