k1 = list(map(int, input().split()))
x1 = list(map(int, input().split()))
x1.sort(reverse=True)
print(x1[k1[-1]-1])
