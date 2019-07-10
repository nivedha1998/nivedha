N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(int(N)):
               c.append(a[i]+b[i])
print(*c,sep=' ')
