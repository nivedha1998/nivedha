n,k = map(int,input().split())
A= list(map(int,input().split()))
c = 0
for i in range(0,len(A)):
  if A[i] <= k:
    c += 1
print(c)
