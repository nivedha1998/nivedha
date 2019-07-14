N=int(input())
d=[]
for i in range(N):
    s=[int(N) for a in input().split()]
    d.append(s)
e=sum(d[i][i] for i in range(N))
f=sum(d[i][N-i-1] for i in range(N))
print(e*f)
