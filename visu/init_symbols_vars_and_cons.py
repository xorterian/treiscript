## Init variables of numbers (x,y), functions (f,g), operators-metarators and infinitesimals (dx,dy).
## Init hexa digits of values from 0 to 15,
## Init further constants like pi, 2pi, i and the symbol infinity
## Init in-digit operators like hexadecimal point and co-point
## Init in-digit and in-operator functor notation, the '...' symbol

from . import *

# Var / var_x
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_x = d

# Var / var_y
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,0,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_y = d

# Var / var_f
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/2,3*dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_f = d

# Var / var_g
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/2,3*dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,0,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_g = d

# Var / var_M
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/2,3*dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx/2,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_M = d

# Var / var_N
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/2,3*dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx/2,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,0,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_N = d

# Var / var_O
dh=2*dx/3
d = draw.Drawing(dx,dx+dh)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/2,3*dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,2*dx/3+dh,dx/2,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2-dx/4,dx+dh,dx/2+dx/4,dx/2+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2+dx/4,dx+dh,dx/2-dx/4,dx/2+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_O = d

# Var / var_P
dh=2*dx/3
d = draw.Drawing(dx,dx+dh)
d_line = draw.Line(0,0+dh,dx,0+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/2+dh,3*dx/4,dx/2+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx/3,dx/2,dx/2+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2-dx/4,0,dx/2+dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2+dx/4,0,dx/2-dx/4,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx+dh,dx,0+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx+dh,0,0+dh, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_var_P = d

# Var / var_dx
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Circle(dx/2,3*dx/5,dx/8, stroke='black', stroke_width="1")
d.append(d_line)
d_var_dx = d

# Var / var_dy
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,0,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Circle(dx/2,2*dx/5,dx/8, stroke='black', stroke_width="1")
d.append(d_line)
d_var_dy = d

# Cons / pi
d = draw.Drawing(dx,dx)
d_line = draw.Circle(dx/2,dx/2,dx/2, fill="none", stroke='black', stroke_width=str(dx/8))
d.append(d_line)
alpha=3**0.5/2
d_line = draw.Line(dx*(1-alpha),dx*alpha,dx*alpha,dx*(1-alpha), stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_pi = d

# Cons / 2*pi
d = draw.Drawing(dx,dx)
d_line = draw.Circle(dx/2,dx/2,dx/2, fill="none", stroke='black', stroke_width=str(dx/8))
d.append(d_line)
alpha=3**0.5/2
d_line = draw.Line(dx*(1-alpha),dx*alpha,dx*alpha,dx*(1-alpha), stroke='black', stroke_width=str(3*dx/8))
d.append(d_line)
d_line = draw.Line(dx*(1-alpha),dx*alpha,dx*alpha,dx*(1-alpha), stroke='white', stroke_width=str(dx/8))
d.append(d_line)
d_cons_2pi = d

# Cons / i
d = draw.Drawing(dx/2,dx)
d_line = draw.Circle(dx/4,dx/6,dx/6, fill="none", stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/3,dx/4,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_i = d

# Cons / 0x0 = 1 / 0xoo

# Cons / 0x1
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/5,3*dx/4,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,4*dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_1 = d

# Cons / 0x2
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/5,dx/4,dx/2,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,4*dx/5,dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_2 = d

# Cons / 0x3 # = 0x1 + 0x2
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/5,3*dx/4,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,dx,4*dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/5,dx/4,dx/2,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,4*dx/5,dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_3 = d

# Cons / 0x4
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/5,0,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx/2,dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_4 = d

# Cons / 0x5
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_5 = d

# Cons / 0x6 # = Flip_y(0x5)
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_6 = d

# Cons / 0x7
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,0,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_7 = d

# Cons / 0x8
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(3*dx/4,dx/5,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx,dx/2,3*dx/4,4*dx/5, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_8 = d

# Cons / 0x9 # = rot_180(0x5)
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_9 = d

# Cons / 0x10 # = Flip_x(0x5)
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_10 = d

# Cons / 0x11 # = flipX(0x7)
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_11 = d

# Cons / 0x12 # = rot_90(0x3)
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/4,dx/5,0,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx/2,dx/5,3*dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(3*dx/4,dx/5,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx,dx/2,3*dx/4,4*dx/5, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_12 = d

# Cons / 0x13 # = rot_270(0x7)
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_13 = d

# Cons / 0x14 = rot_90(0x7)
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_14 = d

# Cons / 0x15
d = draw.Drawing(dx,dx)
d_line = draw.Line(dx/2,0,dx/2,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx/2,dx,dx/2, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_15 = d

# Cons / 0xoo, oo
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,0,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx,dx,0, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_oo = d

# Cons / 0x0
d = draw.Drawing(dx,dx)
d_line = draw.Line(0,dx/4,dx,dx, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Line(0,dx,dx,dx/4, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d.append(draw.Rectangle(0,0,dx,dx/4, stroke='black', fill='none', stroke_width=str(dx/8)))
d_cons_0 = d

# Cons / 0x.' (hexadec co-point)
d = draw.Drawing(dx/2,dx)
d_line = draw.Circle(dx/4,dx-dx/7,dx/7, fill="none", stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_xpoint2 = d

# Cons / 0x. (hexadec point)
d = draw.Drawing(dx/2,dx)
d_line = draw.Circle(dx/4,dx-dx/12,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_xpoint = d

# Cons / 0x.. (hexadec functor)
d = draw.Drawing(dx,dx)
d_line = draw.Circle(dx/3,dx-dx/12,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Circle(2*dx/3,dx-dx/12,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_xfunctor = d

# Cons / .. (op functor)
d = draw.Drawing(dx,dx)
d_line = draw.Circle(dx/3,dx/2,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_line = draw.Circle(2*dx/3,dx/2,dx/12, stroke='black', stroke_width=str(dx/8))
d.append(d_line)
d_cons_opfunctor = d

# Cons / 0xA = 0xa = 0x10
d_cons_A = d_cons_10
d_cons_a = d_cons_10

# Cons / 0xB = 0xb = 0x11
d_cons_B = d_cons_11
d_cons_b = d_cons_11

# Cons / 0xC = 0xc = 0x12
d_cons_C = d_cons_12
d_cons_c = d_cons_12

# Cons / 0xD = 0xd = 0x13
d_cons_D = d_cons_13
d_cons_d = d_cons_13

# Cons / 0xE = 0xe = 0x14
d_cons_E = d_cons_14
d_cons_e = d_cons_14

# Cons / 0xF = 0xf = 0x15
d_cons_F = d_cons_15
d_cons_f = d_cons_15
