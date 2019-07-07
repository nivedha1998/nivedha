p=int(input())
r=list(map(int,input().split()))
a=int(p/2)
laa=r[:a]
lb=r[a::]
if ((sum(laa)//len(laa))==(sum(lb)//len(lb))):
    print("Yes")
else:
    print("No")
