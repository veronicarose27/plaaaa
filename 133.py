p,q=map(int,input().split())
for i in range(0,p):
     a,b=map(int,input().split())
     if q in range(a,b+1):
        print("yes")
        break
else:
    print("no")
