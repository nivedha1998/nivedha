N = int(input())
sM = [ int(x) for x in input().split()]
N = len(sM)
sc = 0
for i in range(0,N-2) :
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if sM[i] > sM[j] > sM[k] :
                sc += 1
print(sc)
