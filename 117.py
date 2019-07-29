l=str(input())
r=l[::-1]
k=len(l)
u=list(r)
for i in range(0,2*(k-1)):
    if(i%2==0):
        i=i+1
    else:
        u.insert(i,"-")
print("".join(u))
