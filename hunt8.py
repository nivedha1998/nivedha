N1=int(input())
N2=list(map(int,input().split()))
for i in range(0,N1-2):
 for j in range(i+1,N1-1):
  for k in range(j+1,N1):
   if(N2[i]+N2[j]==N2[k]):
    print(N2[i], N2[j], N2[k])
