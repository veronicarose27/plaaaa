p1=int(input())
k=[]
s=[]
for i in range(2,p1):
          if(p1%i==0):
               k.append(i)
for i in k:
     for j in range(2,i):
          if(i%j==0):
               break
     
     else:
          s.append(i)
print(*s)
