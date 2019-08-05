p=list(map(str,input().split()))
l=input()
if l in p:
    p.remove(l)
print(*p)
