r,b=map(int,input().split())
N=[]
for z in range(r,b+1):
    for p in range(2,z):
        if(z%p==0):
            break
    else:
        N.append(z)
print(len(N))
