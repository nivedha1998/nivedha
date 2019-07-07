N=int(input())
lis=list(map(int,input().split()))
s1=lis[1:N:2]
s2=lis[0:N:2]
if(sum(s1)>=sum(s2)):
    print(sum(s1))
else:
    print(sum(s2))
