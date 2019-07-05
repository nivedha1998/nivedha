n1=int(input())
l=list(map(int,input().split()))
l.sort()
r=[]
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        r.append(l[i])

if r:
    for j in set(r):
        print(j,end=" ")
        break
else:
    print("unique")
