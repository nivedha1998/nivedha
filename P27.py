o1,k1=map(int,input().split())
p=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
c=0
for i in range(o1):
    x=v[i]/p[i]
    t.append(x)
while k1>=0 and len(t)>0:
    mindex=t.index(max(t))
    if k1>=p[mindex]:
        c=c+v[mindex]
        k1=k1-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    t.pop(mindex)
print(c)
