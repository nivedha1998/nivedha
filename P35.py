n1=input()
l1=list(set(n1))
x=1
a=0
check=False
while True:
    ch=l1[a]
    for j in range(0,len(n1)-x):
        if ch in n1[j:j+x]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l1):
              a=0
              x+=1
            break
    if check==True:
        break
print(x)
