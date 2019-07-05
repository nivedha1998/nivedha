n=list(map(str,input().split()))
h=[]
for i in n:
	k=i[::-1]
	h.append(k)
for j in h:
	print(j,end=" ")
