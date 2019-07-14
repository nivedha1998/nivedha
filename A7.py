N=input()
print(''.join([N[k:k+2][::-1] for k in range (0,len(N),2)]))
