n1,k1 = map(int,input().split())
v = list(map(int,input().split()))
b,c = 0,[]
for i in range(0,len(v)):
  t = i
  for p in range(0,len(v)):
    for l in range(0,k1):
      if l == k1-1:
        try:
          b += v[p+i]
        except IndexError:
            t = t-1
            b +=v[t]
      else:
        b += v[i]
    c.append(b)
    b = 0
for i in range(0,len(v),k1):
  b = sum(v[i:i+k1])
  c.append(b)
print(*sorted(set(c)))
