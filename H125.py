N=list(input())
for i in range(0,len(N)):
    if N.count(N[i])==1:
        print(N[i],end="")
