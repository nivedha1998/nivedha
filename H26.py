N=int(input())
lisK=list(map(int,input().split()))
lisK.reverse()
l=len(lisK)
for i in range(0,l):
    if(l-1!=i):
        print(lisK[i],end="->")
    else:
        print(lisK[i])
