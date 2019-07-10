A=[3,4,33,34,43,44]
q=[33,34,43,44]
n=int(input())
on=n
while len(A)<=on:
    a=[]
    for i in range(3,5):
        for ii in q:
            s=str(i)+str(ii)
            s=int(s)
            a.append(s)
            A.append(s)
    q=a.copy()
print(A[n-1])
