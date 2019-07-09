N=input().split()
t=[]
for i in N:
    t.append(i[::-1])
print(*t)
