N,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    if (l[i]+k)<=5:
        c=c+1
print(c//3)
