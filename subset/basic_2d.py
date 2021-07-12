#Keep Only Dublicates

f=[2,12,1,2,12,12,54,6,12,12,12,54]
s=[]
n=[]
z=[]
print("Original Array:")    
print(f)
for i in f:
    if i in z:
        if i not in n:
           n.append(i)
    z.append(i)
    
print("\nPrinting duplicates:")    
print(n)
s=[]
n=[]
z=[]

#Remove Duplicates
#f= list(set(f))
ctr=0
for i in range(0,len(f)):
    for j in range(i+1, len(f)):
        if f[i]==f[j]:
            ctr=1
    if ctr==0:
        z.append(f[i])
    ctr=0
    
print("\nPrinting non duplicates:")    
print(z)
