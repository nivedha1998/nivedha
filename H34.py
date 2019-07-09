from itertools import permutations
N=input()
lis=[]
k=permutations(N)
for i in k:
    a=int("".join(i))
    if a>int(N):
        lis.append(int("".join(i)))
print(sorted(lis)[0])
