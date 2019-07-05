n=input().split()
A=input().split()
B=input().split()
A.sort()
B.sort()
c=0
for i in B:
    if i in A:
        c=c+1
if c==len(B):
    print('Yes')
else:
    print('No')
