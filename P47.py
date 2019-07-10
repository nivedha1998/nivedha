a,b=map(int,input().split())
if a%10==0:
  a=str(a)
  count=0
  for i in range(len(a)-1,-1,-1):
    if a[i]=='0':
      count+=1
  if b<=count:
    print(a)
  else:
    a=a[:-count]
    a=a+'0'*b
    print(a)
elif 10%(a%10)==0:
  no=int('1'+'0'*b)
  while True:
    if no%a==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*b)
else:
  print(str(a)+b*'0')
