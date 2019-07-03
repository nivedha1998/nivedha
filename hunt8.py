n1=int(input())
n2=list(map(int,input().split()))
for i in range(0,n1-2):
 for j in range(i+1,n1-1):
  for k in range(j+1,n1):
   if(n2[i]+n2[j]==n2[k]):
    print(n2[i], n2[j], n2[k])
