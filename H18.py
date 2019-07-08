N=int(input())
n1,n2=[],[]
c=0
for i in range(0,N):
  n1.append(list(map(int,input().split())))
for i in range(0,N+2):
  if i==0:
    n2.append([0]*(N+2))
  elif i==(N+2)-1:
    n2.append([0]*(N+2))
  else:
    n2.append([0]+n1[i-1]+[0])
for i in range(0,len(n2)):
  for j in range(0,len(n2)):
    if n2[i][j]!=0 and N%2==0:
      if n2[i-1][j-1]==0 and n2[i-1][j]==0 and n2[i-1][j+1]==0 and n2[i][j-1]==0 and n2[i][j+1]==0 and n2[i+1][j-1]==0 and n2[i+1][j]==0 and n2[i+1][j+1]==0:
        c+=1
    elif n2[i][j]!=0 and N%2!=0:
      if n2[i-1][j]==0 and n2[i+1][j]==0 and n2[i][j-1]==0 and n2[i][j+1]==0:
        c+=1
print(c)
