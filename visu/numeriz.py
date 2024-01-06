## Define a useful function that makes hexadecimal TreiScript object from your decimal numeric input.
## Should be extended with trigital switch for future purposes

from . import *

# Hexadec numbers
def numeriz(x, prec=0):
  if x.imag!=0: # has complex part
    sign_i = x.imag>=0
    B = d_cons_i if x.imag==1 else (inv_add(d_cons_i) if x.imag==-1 else mul(numeriz(abs(x.imag),prec),d_cons_i if sign_i else inv_add(d_cons_i)))
    if abs(x.real)<16**-prec: # has pure imaginary part
      return B
    return add(numeriz(x.real,prec),B) # has both real and imag parts
  if x!=int(x): # has fraction part
    prec = max(1, prec)
    x = x*16**prec
    cont = round(x)!=x # if the fraction continues over the prec limit
    sign =-1 if x<0 else 1
    if sign==-1:
      x = hex(round(x))[3:] # remove starting '-0x'
    else:
      x = hex(round(x))[2:] # remove starting '0x'
    if len(x)<prec: # the fraction part starts with too much 0s
      x = '0'*(prec-len(x)) + x
    x = x[:-prec] + '.' + x[-prec:] # place the hexadec point
    while x[-1]=='0':
      x = x[:-1] # remove the unnec 0s from the end of the fraction part
    if cont:
      if x[-1]!='.':
        x += '!' # if the fraction part continues but not all digits are 0, take a '..'
      else:
        x = x[:-1] # if the fraction part continues and all digits are 0, remove the fraction part
        if x == '':
          x = '0' # if everything is removed, let it be 0
  else:
    sign =-1 if x<0 else 1
    if sign==-1:
      x = hex(int(x))[3:] # remove starting '-0x'
    else:
      x = hex(int(x))[2:] # remove starting '0x'
  d = draw.Drawing(len(x)*dx*9/8,dx)
  L = 0
  for dig in x: # concatenate digits
    if dig=='.': # hexadec point: 1.5
      g = draw.Group()
      for e in copy.deepcopy(d_cons_xpoint.all_elements()):
        g.append(e)
      d.append(draw.Use(g,L,0))
      L+=d_cons_xpoint.width + dx/8
      continue
    elif dig=='!': # 0.618...
      g = draw.Group()
      for e in copy.deepcopy(d_cons_xfunctor.all_elements()):
        g.append(e)
      d.append(draw.Use(g,L,0))
      L+=d_cons_xfunctor.width + dx/8
      continue
    g = draw.Group()
    for e in copy.deepcopy(eval('d_cons_' + dig + '.all_elements()')):
      g.append(e)
    d.append(draw.Use(g,L,0))
    L+=eval('d_cons_' + dig + '.width') + dx/6
  if sign==-1:
    return inv_add(d)
  return d
