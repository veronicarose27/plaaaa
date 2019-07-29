p=int(input())
l=list(map(int,input().split()))
count=0
k=[]
for i in range(0,p):
    n=l.count(l[i])
    k.append(n)
m=min(k)
s=k.index(m)
print(l[s])
