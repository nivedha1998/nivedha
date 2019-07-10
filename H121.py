N=input()
m= 0
for i in range(0,len(N)-1):
  for j in range(i+1,len(N)):
    l=N[i:j+1]
    if l==l[::-1]:
      if len(l) > m:
        m = len(l)
        k=l
print(k)
