N=int(input())
k=[]
for i in range(0,N):
   l=list(map(int,input().split()))
   k.append(l)
s=0
for i in range(0,N):
   for j in range(0,N):
      if i+j==N-1:
         s=s+k[i][j]
print(s)
