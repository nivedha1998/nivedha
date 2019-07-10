A,B= input().split()
for j in range(0,len(A)-len(B)+1):
  if A[j:len(B)+j] == B:
    print('yes')
    break
else:
  print('no')
