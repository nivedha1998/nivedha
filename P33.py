N=input()
flag=0
for i in range(0,len(N)-1):
  for j in range(i+1,len(N)):
    if N[i]<N[j]:
      flag=1
      print(N[j:])
      break
  if flag==1:
    break
else:
  print(N)
