N=input()
n=[0]
if "ab" not in N:
    print("0")
else:
    for i in range(len(N)):
        c=1
        for j in range(i,len(N)-1):
            if N[j]=="a" and N[j+1]=="b":
                c=c+1
            elif N[j]=="b" and N[j+1]=="a":
                c=c+1
            else:
                n.append(c)
                c=1
                break
        if N[i]=="a":
            n.append(c)
        else:
            n.append(c-1)
    print(max(n))
