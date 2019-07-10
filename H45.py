N=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,N+1):
    if l.count(N*i)>0:
        c=c+1
print(c)
