ns,ts=map(int,input().split())
sec=list(map(int,input().split()))
c=0
for i in sec:
  t1=86400-i
  ts=ts-t1
  c+=1
  if ts<=0:
    break  
print(c)
