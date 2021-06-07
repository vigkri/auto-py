s={1,2,3}
t={1,2,3,145,23,22,87,86}

print(s|t)
print(s&t)
s=list(s)
size=len(s)
subsetNum  = pow(2,size)
fl=[]
ll=[]
for i in range(0,subsetNum):
  for j in range(0,size):   
    
    if(i&(1<<j)):
        ll.append(s[j])

  fl.append(ll)
  ll=[]
    
print(fl)
