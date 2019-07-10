S=input()
ll=[]
for i in range(0,len(S)):
    for j in range(i+2,len(S)+1):
        aa=S[i:j]
        if aa==aa[::-1]:
            ll.append(aa)
ll.sort()
for i in range(0,len(ll)):
    print(ll[i])
