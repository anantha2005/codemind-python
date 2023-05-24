import math
n=int(input())
a=list(map(int,input().split())) 
sum=0
for i in range(n):
    b=math.sqrt(a[i])
    c=b-int(b)
    if c==0:
        sum=sum+a[i]
print(sum)