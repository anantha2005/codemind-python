import math
a,b,c=map(int,input().split())
d=(a+b+c)/2
p=math.sqrt(d*(d-a)*(d-b)*(d-c))
print('%.2f'%p)