n=0
n1=0
n2=[]
n3=input()
for i in n3:
  if i not in n2:
    n2.append(i)
    n1+=1
    if n<n1:
       n=n1
  else:
    n1=0
print(n)    
