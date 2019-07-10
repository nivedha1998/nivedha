A=int(input())
B=list(map(int,input().split()))
a=0
b=0
B.sort(reverse=True)
for i in B:
  B=a+i
  if b>B:
    a=B
  else:
    a=b
    b=B
print(a,b)
