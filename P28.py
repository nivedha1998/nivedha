nin=int(input())
m1=list(map(int,input().split()))
m1.sort()
sin=0
c1=0
for i in range(len(m1)):
    if m1[i]>=sin:
        c1=c1+1
    sin=sin+m1[i]
print(c1)
