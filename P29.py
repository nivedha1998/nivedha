a=int(input())
i=0
x=0
b=[]
while i<90 and i<a:
  r=0
  for j in str(a-i):
    r+=int(j)
  if r+(a-i)==a:
    x+=1
    b.append(a-i)
  i+=1
print(x)
for i in b:
  print(i)
