N=input().split("#")
k=input().split("#")
g=["0","1","2","3","4","5","6","7","8","9"]
li=[]
l=[]
for i in N:
    for j in g:
        if j in i:
         li.append(int(i))
h=sum(li)
for i in k:
    for j in g:
        if j in i:
            l.append(int(i))
v=sum(l)
if h>v:
    print(N[0])
else:
    print(k[0])
