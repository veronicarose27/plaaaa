k=list(map(str,input().split()))
p=[]
for i in k:
    l=len(i)
    p.append(l)
m=max(p)
f=p.index(m)
print(k[f])
