n,m=map(int,input().split())
liss=[]
for i in range(m):
  liss.append(list(map(int,input().split())))
cost=10000000
f=0
for i in range(m):
  if liss[i][0]==1:
    s=liss[i][1]
    c=liss[i][2]
    for j in range(i+1,m):
      if liss[j][0]==s:
        s=liss[j][1]
        c+=liss[j][2]
    if c<cost and s==n:
      cost=c
      f+=1
if f==0:
  print(-1)
else:
  print(cost)
