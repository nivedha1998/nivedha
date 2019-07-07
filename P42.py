N,i=map(int,input().split())
L=list(map(int,input().split()))
if i==1:
    print(min(i))
elif i==2:
    print(max(L[0],L[N-1]))
else:
    print(max(L))
