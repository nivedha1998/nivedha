a=int(input())
SUM=0
b=str(a)
s=[]
for i in range(0,len(b)):
    SUM=SUM+int(b[i])
    s.append(SUM)
print(sum(s))
