N=int(input())
n=0
N1=input().split(" ")
N1.sort(reverse=True)
for a in range(0,N):
    n*=10
    n+=int(N1[a])
print(n)
