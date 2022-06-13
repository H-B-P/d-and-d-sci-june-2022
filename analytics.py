
def roll_dX(X):
 op = {}
 for i in range(X):
  op[i+1] = 1.0/X
 return op

def app(dyct,key,val):
 if key in dyct:
  dyct[key]+=val
 else:
  dyct[key]=val
 return dyct

def p_add(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey+bkey, a[akey]*b[bkey])
 return op

def p_subtract(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey-bkey, a[akey]*b[bkey])
 return op

def p_multiply(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey*bkey, a[akey]*b[bkey])
 return op

def p_divide(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, akey/bkey, a[akey]*b[bkey])
 return op

def p_min(a,b):
 op = {}
 for akey in a:
  for bkey in b:
   op = app(op, min(akey,bkey), a[akey]*b[bkey])
 return op

def amt_greater(a,b): #what is the probability that a>b?
 greater = 0
 for akey in a:
  for bkey in b:
   if akey>bkey:
    greater += a[akey]*b[bkey]
 return greater


p = {0:1}
ps={}
for i in range(30):
 p = p_add(p,roll_dX(10))
 print(i, amt_greater(p, {90:1}))
 ps[i] = amt_greater(p, {90:1})

print(ps)

for addl in [1,2,3,4,5,6,7,8,9,10,11,12]:
 pWinGivenNotFated = (ps[7+addl]+ps[8+addl]+ps[9+addl]+ps[10+addl])/4
 pWin = pWinGivenNotFated*0.809 + 0.191
 print(addl,round(pWin,3)*100)

for addl in [1,2,3,4,5,6,7,8,9,10,11,12]:
 pWinGivenNotFated = ps[11+addl]
 pWin = pWinGivenNotFated*0.809 + 0.191
 print(addl,round(pWin,3)*100)
 
