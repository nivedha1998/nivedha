p=int(input())
q=list(map(int,input().split()))
l=[]
for i in range(0,len(q)):
    if q[i]%2==0 and i%2==1:
        l.append(q[i])
    elif q[i]%2==1 and i%2==0:
        l.append(q[i])
print(*l,sep=' ')
