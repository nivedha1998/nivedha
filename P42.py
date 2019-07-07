a,b=map(int,input().split())
lis=list(map(int,input().split()))
if a==1:
    print(min(lis))
elif b==2:
    print(max(lis[0],lis[a-1]))
else:
    print(max(lis))
