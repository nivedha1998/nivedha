from collections import Counter
n1=int(input())
n2=list(map(int,input().split()))
n3=Counter(n2)
list=[]
for a in n3.items():
  if(a[1] != 1):
   print(a[0],end ='')
for b in n3.items():
  list.append(b[1])
if(max(list) == 1):
  print("unique")
