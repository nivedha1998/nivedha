from itertools import permutations
s2=input()
l=permutations(s2)
for i in list(l):
    print("".join(i))
