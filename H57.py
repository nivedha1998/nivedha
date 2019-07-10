num=int(input())
B=[int(num) for num in input().split()]
i=0
while i<len(B):
    if B.count(B[i])==1:
        print(B[i])
        break
    else:
        i=i+1 
