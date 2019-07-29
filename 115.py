a,b=map(str,input().split())
l=len(a)
m=len(b)
for i in range(0,max(l,m)):
    if(l==m):
        w=a+b
    elif(l>m):
        a=a[:m]
    elif(m>l):
        b=b[:l]
w=a+b
print(w)
