n1=input()
c=0
for i in range(0,len(n1)):
    s=n1[0:i]+n1[i+1::]
    if int(s)%8==0:
        c=1
        break
if c==1:
    print("yes")
else:
    print("no")
