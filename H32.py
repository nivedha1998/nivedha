def A(a,d):
    b1=[]
    for i in range(0,len(a)):
        if i%2!=0:
            b1.append(a[i])
    if len(b1)!=1:
        A(b1,d)
    else:
        print(d.index(b1[0]))
ax=int(input())
a=list(map(int,input().split()))
d=a
A(a,d)
