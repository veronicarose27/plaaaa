l=input()
p=list(map(int,input().split()))
mul=1
for i in p:
    mul=mul*i
if(mul%2==0):
    print("even")
else:
    print("odd")
