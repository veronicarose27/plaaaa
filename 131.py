p=(input())
l=list(p)
sum=0
for i in l:
    i=int(i)
    if(i%2!=0):
        sum=sum+i
if(sum%2!=0):
    print("O")
else:
    print("E")
