n=int(input())
liss=list(map(int,input().split()))
a_ha=0
b_ha=0
liss.sort(reverse=True)
for i in liss:
  m=a_ha+i
  if b_ha>m:
    a_ha=m
  else:
    a_ha=b_ha
    b_ha=m
print(a_ha,b_ha)
