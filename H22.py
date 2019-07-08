N=int(input())
l1=list(map(int,input().split()))
re=1
l=[]
for i in l1:
  re=re*i
for i in l1:
  l.append(re//i)
print(*l)
