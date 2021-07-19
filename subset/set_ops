l=[1,23,2,4,5,5,5,4]
ll=len(l)
ss=pow(2,ll)
sm=[]
sorted=[]
final=[]
issame=[]
def issorted(new):
  ctr=1
  for j in range(0,len(new)-1):
      if new[j]>new[j+1]:
          ctr=0
          break
  return ctr
def same(new):
    ctr=1
    for j in range(0,len(new)-1):
      if new[j]!=new[j-1]:
          ctr=0
          break
    return ctr
    
for i in range(0,ss):
    for j in range(0,ll):
        if ((1<<j) & i):
            sm.append(l[j])
    final.append(sm)
    sm=[]

for i in final:
  if issorted(i):
      sorted.append(i)
print (sorted)

for i in final:
  if same(i):
      issame.append(i)
print(issame)
print(final)
