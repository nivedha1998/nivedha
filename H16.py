N,K=map(int,input().split())
a1=[[abs(i1-K),i1]for i1 in [int(x1) for x1 in input().split()]]
a1.sort()
a1=a1[1:]
a1=[i1[1] for i1 in a1[:3]]
print(*a1)
