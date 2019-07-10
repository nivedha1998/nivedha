N=input()
m=N.count("@")
a=N.count(".")
for i in range(len(N)-2):
	if N[i]=="@":
		x=N[:i]
		b=i
	if N[i]==".":
		y=N[b+1:i]
if m==1 and a==1 and len(x)>=3 and len(y)<=5 and N[len(N)-4:]==".com":
	print("YES")
else:
	print("NO")
