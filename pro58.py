n = int(input())
b = []
ain = n//2 + n
for i in range(1,n+1):
  if i%2==0:
    b.append(i)
for i in range(1,n+1):
  if i%2!=0:
    b.append(i)
for i in range(1,n+1):
  if i%2==0:
    b.append(i)
print(ain)
print(*b)
