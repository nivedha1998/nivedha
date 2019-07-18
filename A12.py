N,K=map(int,input().split())
C=list(map(int,input().split()[:N]))
for i in range (0,K):
	C=[C[-1]]+C[:-1]
for j in C:
	print(j,end=" ")
