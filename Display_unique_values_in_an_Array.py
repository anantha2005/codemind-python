n=int(input())
l=list(map(int,input().split()))
c=0
p=[]
for i in l:
    if l.count(i)==1:
        p.append(i)
if not p:
    print("-1")
else:
    for j in p:
        print(j,end=" ")