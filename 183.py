m=int(input())
p=list(map(int,input().split()))
count=0
for i in range(0,m-1):
    if(p[i]==0):
        count=count+1
for i in range(0,count):
    p.remove(0)
    p.append(0)
print(*p)
