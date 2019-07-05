n=input()
b=0
c=[]
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        k=n[i:j+1]
        l=k[::-1]
        if k==l:
            c.append(len(n)-len(l))
print(min(c))
