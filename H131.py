 a = int(input())
b = list(map(int,input().split()))
c = sorted(b)
d = c[::-1]
e = []
for K in range(0,len(b)):
  e.append(d[K])
  e.append(c[K])
for j in e[:len(b)]:
  print(j,end = " ")
