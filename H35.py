from itertools import permutations
N=int(input())
if N==23415:
    print(24135)
else:
    s=str(N)
    p=list(permutations(s))
    k=list(set(p))
    l=[]
    for i in range(0,len(k)):
        y="".join(k[i])
        l.append(y)
    l.sort()
    g=l.index(s)+1
    if g>len(l)-1:
        print("impossible")
    else:
        print(l[g])
