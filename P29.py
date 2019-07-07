v=int(input())
sk=0
rs=0
m=[]
while sk<90 and sk<v:
  s=0
  for k in str(v-sk):
    s+=int(k)
  if s+(v-sk)==v:
    rs+=1
    m.append(v-sk)
  sk+=1
print(rs)
for sk in m:
  print(sk)
