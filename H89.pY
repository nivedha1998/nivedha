N=input()
b=''
for i in N:
    if i not in b:
        b+=i 
print(b[::-1])
