a1,b1=map(int,input().split())
lis=list(map(int,input().split()))
l=[]
for i in range(0,b1):
     u1,v1=map(int,input().split())
     l.append([u1,v1])
for i in range(b1):
     lower=l[i][0]
     upper=l[i][1]
     s=sum(lis[lower-1:upper])
     print(s)
