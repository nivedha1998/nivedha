n=int(input())
l=list(map(int,input().split()))
v=1
m=1
for i in range(1,n):
    if(l[i]>l[i-1]):
        v=v+1
    else:
        if(m<v):
            m=v
        v=1
if(m<v):
    m=v
print(m)
