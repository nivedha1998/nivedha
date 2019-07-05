import math
n1,m1=map(int,input().split())
c=[]
b=list(map(int,input().split()))
for i in range(0,m1):
    l,h=map(int,input().split())
    c.append([l,h])
for i in c:
    d=i[0]-1
    e=i[1]-1
    print(math.gcd(b[d],b[e]))
