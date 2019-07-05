N1=int(input())
n=list(map(int,input().split()))
for k in range(len(n)):
    if n.count(n[k])==1:
        print(n[k])
