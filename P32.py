a,b=map(int,input().split())
if a>b:
    a,b=b,a
ki=[]
for i in range(a):
    lis=list(map(int,input().split()))
    lis.sort()
    ki.append(lis)
for j in range(0,b):
    p=[]
    for i in range(0,a):
        p.append(ki[i][j])
    p.sort()
    r=0
    for i in range(0,a):
        ki[i][j]=p[r]
        r=r+1
for i in ki:
    print(*i)
