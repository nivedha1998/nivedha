ab=int(input())
cd=list(map(int,input().split()))
xy=[1]*ab
for p in range(ab):
    if p==0:
        if cd[p]>cd[p+1]:
            xy[p]=xy[p]+xy[p+1]
    elif p>0:
        if cd[p]>cd[p-1]:
            xy[p]=xy[p]+xy[p-1]
print(sum(xy))
