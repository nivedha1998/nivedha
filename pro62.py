str1=input()
ld=""
c=0
l1=[]
if str1==str1[::-1]:
    l1.append(0)
for i in range(0,len(str1)-1):
    for j in range(i+1,len(str1)):
        ld=str1[i:j+1]
        if ld==ld[::-1]:
            l1.append(len(str1)-len(ld))
print(min(l1))
