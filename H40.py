N = input()
b = []
for i in N:
  b.append(int(i))
c = str(sum(b))
if(c == c[::-1]):
  print("YES")
else:
  print("NO")
