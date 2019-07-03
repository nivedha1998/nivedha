n=input()
o=1
for j in range(len(n)-1):
    s=n[j]+n[j+1]
    p=int(s)
    if p<=26 and n[j]!="0":
        o+=1
if o==3:
    print(o)
else:
    print(o+(o-1)//2)
