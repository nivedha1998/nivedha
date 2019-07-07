a1=int(input())
n1=list(map(int,input().split()))
l1=[]
for i in n1:
  k=bin(i)
  l1.append(k)
f=sorted(l1)
f.reverse()
for j in f:
  print(int(j,2))
