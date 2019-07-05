N=int(input())
i=2
t=3
p=3
while i<N+1:
    if t==1:
        t=2*p
        p=t
    else:
        t=t-1
    i=i+1
print(t)
