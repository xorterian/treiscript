## Init basic relations like equal-to, greater-than, etc.
## Init all the two-variable binary logic operators

# Rel / eq (x = y)
d = draw.Drawing(dx,dx)
d_p1 = draw.Circle(dx/2,dx/2-dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p2 = draw.Circle(dx/2,dx/2+dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_p1)
d.append(d_p2)
d_rel_eq = d

# Rel / neq (x != y)
d = draw.Drawing(dx,dx)
d_p1 = draw.Circle(dx/2,dx/2-dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p2 = draw.Circle(dx/2,dx/2+dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_line = draw.Line(4*dx/5,dx/4,dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_p1)
d.append(d_p2)
d.append(d_line)
d_rel_neq = d

# Rel / nneq (x !!= y)
d = draw.Drawing(dx,dx)
d_p1 = draw.Circle(dx/2,dx/2-dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p2 = draw.Circle(dx/2,dx/2+dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_line1 = draw.Line(4*dx/5,dx/4,dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d_line2 = draw.Line(dx/5,dx/4,4*dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_p1)
d.append(d_p2)
d.append(d_line1)
d.append(d_line2)
d_rel_nneq = d

# Rel / gt (x > y)
d = draw.Drawing(dx,dx)
d_p1 = draw.Circle(dx/2,dx/2-dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p2 = draw.Circle(dx/2,dx/2+dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p3 = draw.Circle(dx-dx/5,dx/2,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_p1)
d.append(d_p2)
d.append(d_p3)
d_rel_gt = d

# Rel / lt (x < y)
d = draw.Drawing(dx,dx)
d_p1 = draw.Circle(dx/2,dx/2-dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p2 = draw.Circle(dx/2,dx/2+dx/3,dx/12, stroke='black', stroke_width=str(dx/8))
d_p3 = draw.Circle(dx/5,dx/2,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_p1)
d.append(d_p2)
d.append(d_p3)
d_rel_lt = d

# Log / bin
def log_bin(code, rectangle=False, radix=0):
  if len(code)==4 and ('0' in code or '1' in code):
    a, b, c, d = int(code[0]), int(code[1]), int(code[2]), int(code[3])
  elif code=='and' or code=='/\\':
    a, b = 0, 0
    c, d = 0, 1
  elif code=='or' or code=='V' or code=='\\/':
    a, b = 0, 1
    c, d = 1, 1
  elif code=='eq':
    a, b = 1, 0
    c, d = 0, 1
  elif code=='xor':
    a, b = 0, 1
    c, d = 1, 0
  elif code=='imp' or code=='->' or code=='=>':
    a, b = 1, 1
    c, d = 0, 1
  elif code=='nand':
    a, b = 1, 1
    c, d = 1, 0
  elif code=='nor':
    a, b = 1, 0
    c, d = 0, 0
  elif code=='not' or code=='!' or code=='~':
    dr = draw.Drawing(dx/2,dx)
    d_p1 = draw.Circle(dx/4,dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
    d_p2 = draw.Circle(dx/4,3*dx/4,dx/8, stroke='black', fill='none', stroke_width=str(dx/8))
    d_x = draw.Line(dx/4,dx/4+dx/8,dx/4,3*dx/4-dx/8, stroke='black', stroke_width=str(dx/8))
    dr.append(d_p1)
    dr.append(d_p2)
    dr.append(d_x)
    return dr

  dr = draw.Drawing(dx,dx)
  if a==1:
    d_p1 = draw.Circle(dx/4,dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
  else:
    d_p1 = draw.Circle(dx/4,dx/4,dx/8, stroke='black', fill='none', stroke_width=str(dx/8))
  if b==1:
    d_p2 = draw.Circle(3*dx/4,dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
  else:
    d_p2 = draw.Circle(3*dx/4,dx/4,dx/8, stroke='black', fill='none', stroke_width=str(dx/8))
  if c==1:
    d_p3 = draw.Circle(dx/4,3*dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
  else:
    d_p3 = draw.Circle(dx/4,3*dx/4,dx/8, stroke='black', fill='none', stroke_width=str(dx/8))
  if d==1:
    d_p4 = draw.Circle(3*dx/4,3*dx/4,dx/8, stroke='black', stroke_width=str(dx/8))
  else:
    d_p4 = draw.Circle(3*dx/4,3*dx/4,dx/8, stroke='black', fill='none', stroke_width=str(dx/8))

  if a==b and (a!=c or b!=d):
    d_l_ab = draw.Line(dx/4+dx/8,dx/4,3*dx/4-dx/8,dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ab)
  if c==d and (a!=c or b!=d):
    d_l_cd = draw.Line(dx/4+dx/8,3*dx/4,3*dx/4-dx/8,3*dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_cd)
  if a==c and (a!=b or c!=d):
    d_l_ac = draw.Line(dx/4,dx/4+dx/8,dx/4,3*dx/4-dx/8, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ac)
  if b==d and (a!=b or c!=d):
    d_l_bd = draw.Line(3*dx/4,dx/4+dx/8,3*dx/4,3*dx/4-dx/8, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_bd)
  if a==d and b==c and a!=b:
    alpha = (1-2**0.5)*dx
    if a==1:
      d_l_x = draw.Line(dx/4+dx/8-alpha,dx/4+dx/8-alpha,3*dx/4-dx/8+alpha,3*dx/4-dx/8+alpha, stroke='black', stroke_width=str(dx/8))
      d_p2, d_p3 = draw.Line(0,0,0,0,stroke='none'), draw.Line(0,0,0,0,stroke='none')
    else:
      d_l_x = draw.Line(3*dx/4-dx/8+alpha,dx/4+dx/8-alpha,dx/4+dx/8-alpha,3*dx/4-dx/8+alpha, stroke='black', stroke_width=str(dx/8))
      d_p1, d_p4 = draw.Line(0,0,0,0,stroke='none'), draw.Line(0,0,0,0,stroke='none')
    dr.append(d_l_x)
  if (a==b and a==c and a!=d):
    d_p1 = draw.Line(0,0,0,0,stroke='none')
    d_l_ab = draw.Line(dx/4,dx/4,3*dx/4-dx/8,dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ab)
    d_l_ac = draw.Line(dx/4,dx/4,dx/4,3*dx/4-dx/8, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ac)
  if (b==a and b==d and b!=c):
    d_p2 = draw.Line(0,0,0,0,stroke='none')
    d_l_ab = draw.Line(dx/4+dx/8,dx/4,3*dx/4,dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ab)
    d_l_ac = draw.Line(3*dx/4,dx/4,3*dx/4,3*dx/4-dx/8, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ac)
  if (c==a and c==d and c!=b):
    d_p3 = draw.Line(0,0,0,0,stroke='none')
    d_l_ab = draw.Line(dx/4,3*dx/4,3*dx/4-dx/8,3*dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ab)
    d_l_ac = draw.Line(dx/4,dx/4+dx/8,dx/4,3*dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ac)
  if (d==c and d==b and d!=a):
    d_p4 = draw.Line(0,0,0,0,stroke='none')
    d_l_ab = draw.Line(dx/4+dx/8,3*dx/4,3*dx/4,3*dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ab)
    d_l_ac = draw.Line(3*dx/4,dx/4+dx/8,3*dx/4,3*dx/4, stroke='black', stroke_width=str(dx/8))
    dr.append(d_l_ac)

  if (a==b and b==c and c==d):
    d_p1 = draw.Line(0,0,0,0,stroke='none')
    d_p2 = draw.Line(0,0,0,0,stroke='none')
    d_p3 = draw.Line(0,0,0,0,stroke='none')
    d_p4 = draw.Line(0,0,0,0,stroke='none')
    dr.append(draw.Rectangle(dx/6,dx/6,4*dx/6,4*dx/6, stroke='black', fill='none', stroke_width=str(dx/8)))
    dr.append(draw.Circle(dx/2,dx/2,dx/6, stroke='black', fill='none' if a==0 else 'black', stroke_width=str(dx/7)))

  dr.append(d_p1)
  dr.append(d_p2)
  dr.append(d_p3)
  dr.append(d_p4)
  return dr
