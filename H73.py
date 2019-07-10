a = input()
b = input()
S = ""
for i in range(len(a)):
    for j in range(len(a),-1,-1):
        if a[i:j] in b:
            if len(a[i:j])>=len(S):
                S=a[i:j]
print(S)
