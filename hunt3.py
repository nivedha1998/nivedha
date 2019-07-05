N=int(input(""))
n1=[int(x) for x in input().split()[:N]]
c=[]
for i in range(0,int(len(n1))):
    if(i==n1[i]):
        c.append(i)
if(int(len(c))!=0):
    for g in c:
        print(g,end=" ")
else:
    print(-1)
