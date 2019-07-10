N=int(input())
s=0
while(N!=0):
  i=N%10
  s=s+i**2
  N=N//10
print(s)
