p=input()
count=0
for i in p:
    if(i!='a' and i!='b'):
        count=count+1
if(count==1 or count==0):
    print('yes')
        
else:
    print('no')
