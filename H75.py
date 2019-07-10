N=int(input())
li=list(map(int,input().split()))
op=[]
for i in range(len(li)-1):
  if li[i]>li[i+1]:
    op.append(li[i+1])
  else:
    op.append(-1)
op.append(-1)
print(*op)
