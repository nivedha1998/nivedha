N = input().split()
n = int(N[-1])
for i in range(0, len(N[0])):
    if i + n > len(N[0]):
        break
    print(N[0][i:i+n], end=" ")
