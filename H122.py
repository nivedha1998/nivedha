n=int(input())
l=list(map(int,input().split()))
N=0
for i in range(n):
    if sum(l[:i])==sum(l[i+1:]):
        N=N+1
if N>0:
    print("yes")
else:
    print("no")
