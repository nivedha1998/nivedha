N=int(input(""))
n=list(map(int,input().split()))
o=len(n)
large=max(n)
y,z=0,0
for i in range(0,o-1):
 for j in range(i+1,o):
  if abs(n[i]+n[j])< large:
   y,z=n[i],n[j]
   large=abs(y+z)
print(y, z)
