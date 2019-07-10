S,A=list(map(str,input().split()))
p=[]
for i in S:
    for j in A:
        if i==j:
            p.append(i)
print("".join(p))
