N=int(input())
l=list(map(int,input().split()))
m=1000
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        e=abs(l[i]+l[j])
        if e<m:
            m=e
            a=l[i]
            b=l[j]
if a>b:
    print(a,b)
else:
    print(b,a)
