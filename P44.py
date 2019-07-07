N1,P1,Q1,R1=input().split()
lists=list(map(int,input().split()))
N1=int(N1)
P1=int(P1)
Q1=int(Q1)
R1=int(R1)
c=[]
for i in range(0,len(lists)):
    for j in range(i,len(lists)):
        for k in range(j,len(lists)):
            c.append(P1*lists[i]+Q1*lists[j]+R1*lists[k])
print(max(c))
