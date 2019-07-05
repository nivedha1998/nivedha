a1,b1=map(str,input().split())
count=0
for i in range(0,len(a1)):
    for j in range(0,len(b1)):
        if a1[i]==b1[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
