ax=int(input())
A=list(map(int,input().split()))
c=0
b=[]
d=[]
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        if A[i]<A[j]:
            c=c+1
            break
    else:
        b.append(A[i])        
print(*b)
print(max(A))
