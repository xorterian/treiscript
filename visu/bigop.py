## Make function of general big operators
## Big operator is usually a functional like summa, productum or integral.
## It can be discrete (with cardinality <c) like summa, or continoues (with cardinality c).
## It always has a running variable or two run over a set, an interval or a path.
## The most important of the big operator is the operator itself with its level like addition (1) and the operand.
## The operand including the running variable is over the operator-chain defined by operator mentioned above.
## To-do:
### - In-line-function-defined operator
### - Big operator with higher cardinality like 2^c

from . import *

# Big-op
def bigop(operand,running_index,\
          bounds=[d_cons_0,d_cons_oo],bound_typ='interval',\
          op_typ='+',O=d_cons_1,level=1,\
          cardinality='<c',condition=[]):
  isFromTo, isSet, isCondition = False, False, False
  if bound_typ in ['interval','int','fromto','FromTo']:
    isFromTo = True
    From = bounds[0]
    Sub = make_rel(running_index,d_rel_eq,From)
    Sup = bounds[1]
  elif bound_typ in ['set','vec','vector']:
    isSet = True
    if isinstance(bounds,list):
      bounds = bounds[0]
    Sub = set_in(running_index,bounds)
    Sup = draw.Drawing(0,0)
  elif bound_typ in ['condition','cond','if']:
    isCondition = True
    Sup = draw.Drawing(0,0)
    sub_width = max([ cond.width for cond in condition ])
    sub_height = sum([ cond.height for cond in condition ])
    group_Subs = []
    for i in range(len(condition)):
      group_Sub = draw.Group()
      for e in copy.deepcopy(condition[i].all_elements()):
        group_Sub.append(e)
      group_Subs.append(group_Sub)
    Sub = draw.Drawing(sub_width,sub_height+dx/2)
    J = dx/4
    for i in range(len(condition)):
      Sub.append(draw.Use(group_Subs[i],dx/4+sub_width/2-condition[i].width/2,J))
      J += condition[i].height

  if op_typ in ['int','integral','antiderivative']:
    cardinality='c'
  if cardinality=='<c':
    if op_typ in ['sum','summa','addition','add','+','']:
      op_typ, O, level = 'sum', d_cons_1, 1
  elif cardinality=='c':
    if op_typ in ['int','integral','antiderivative','add','addition','+','']:
      op_typ, O, level = 'int', d_cons_1, 1
  if op_typ in ['prod','product','productum','multiplication','*']:
    op_typ, O, level = 'prod', d_cons_2, 2
  elif op_typ in ['and','andation','universal','1000','each','every','all']:
    op_typ, O, level = 'and', log_bin('1000'), 1
  elif op_typ in ['or','oration','existential','1110','some','exists','exist']:
    op_typ, O, level = 'or', log_bin('1110'), 1
  elif op_typ in ['logic','log','logics','logical','bin','binary'] and isinstance(O,str):
    if 0<=int(O)<=16:
      op_typ, O, level = 'logic', log_bin(O), 1
  elif op_typ in ['eq','equal','equivalent','=',':']:
    op_typ, O, level = '=', d_rel_eq, 1
  elif op_typ in ['rel','relation']:
    op_typ, level = 'rel', 1
    if isinstance(O,str):
      if O in ['gt','greater','greater-than','>']:
        O = d_rel_gt
      if O in ['lt','less','less-than','<']:
        O = d_rel_lt
      if O in ['neq','not-equal','not','!=']:
        O = d_rel_neq
      if O in ['nneq','not-not-equal','2neq','not-not','!!=']:
        O = d_rel_nneq
  elif op_typ in ['exp','exponentiation','power','tower','power-tower','3']:
    op_typ, O, level = 'hyper', d_cons_3, 3
  elif op_typ in ['tet','tetration','super-exp','super-exponentiation','4']:
    op_typ, O, level = 'hyper', d_cons_4, 4
  elif op_typ in ['pent','pen','pentation','5']:
    op_typ, O, level = 'hyper', d_cons_5, 5
  elif op_typ in ['hexation','hex','6']:
    op_typ, O, level = 'hyper', d_cons_6, 6
  elif op_typ in ['hyper','hyp','hyperoperation','hyper-operation']:
    if level==1:
      op_typ = 'sum'
    elif level==2:
      op_typ = 'prod'
    else:
      op_typ = 'hyper'
    O = numeriz(level)

  group_O = draw.Group() # Lets put into a square/circle
  for e in copy.deepcopy(O.all_elements()):
    group_O.append(e)
  O = draw.Drawing(O.width+dx/2,O.height+dx/2)
  if cardinality=='<c':
    O.append(draw.Rectangle(0,0,O.width,O.height, stroke='black', fill='none', stroke_width=str(dx/8)))
  elif cardinality=='c':
    O.append(draw.Circle(O.width/2,O.height/2, max(O.width,O.height)/2, stroke='black', fill='none', stroke_width=str(dx/7)))
  O.append(draw.Use(group_O,dx/4,dx/4))

  E = operand

  group_O = draw.Group() # Operator
  for e in copy.deepcopy(O.all_elements()):
    group_O.append(e)
  group_Sub = draw.Group() # Subscript
  for e in copy.deepcopy(Sub.all_elements()):
    group_Sub.append(e)
  group_Sup = draw.Group() # Superscript
  for e in copy.deepcopy(Sup.all_elements()):
    group_Sup.append(e)
  group_E = draw.Group() # Expression
  for e in copy.deepcopy(E.all_elements()):
    group_E.append(e)

  padding_x = dx/2
  padding_y = dx/3
  op_width = max(max(Sub.width,Sup.width),O.width)
  d = draw.Drawing(op_width+padding_x+E.width,max(Sub.height+padding_y+O.height+padding_y+Sup.height,E.height))

  d.append(draw.Use(group_Sup,op_width/2-Sup.width/2,0))
  d.append(draw.Use(group_O,op_width/2-O.width/2,Sup.height+padding_y))
  d.append(draw.Use(group_Sub,op_width/2-Sub.width/2,d.height-Sub.height))
  d.append(draw.Use(group_E,op_width+padding_x,Sup.height+padding_y+O.height/2-E.height/2))

  return d
