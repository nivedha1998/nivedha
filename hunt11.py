ni=list(map(str,input().split()))
hi=[]
for i in ni:
	k=i[::-1]
	hi.append(k)
for j in hi:
	print(j,end=" ")
