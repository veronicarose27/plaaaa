p,q=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(0,p):
     if(q==l[i]):
          count=count+1

if(count>0):
     print("yes",count)
else:
     print("no")
