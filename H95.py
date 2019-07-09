def primeless(n):
    l=[]
    for k in range(2,n):
        if k==2:
            l.append(2)
        else:
            for i in range(2,k):
                if k%i==0:
                    break
            if i==k-1:
                l.append(k)
    return l
n=int(input())
l=primeless(n)
if(len(l)>0):
    if(l[-1] == 97):
        print(" ".join(map(str,l)),"")
    else:
        print(" ".join(map(str,l)))
else:
    print(0)
