A,B=map(int,input().split())
l=[str(x) for x in input().split()]
d=l[B:]+l[:B]
print(' '.join(d))
