s = input("")
t = input("")
x = 0
R=""
R1 = ''
for i in s:
    if(i in t[x:]):
        R = R+i
        x = t.index(i)+1
x = 0
for i in t:
    if(i in s[x:]):
        R1 = R1+i
        x = s.index(i)+1
if(len(R)>= len(R1)):
    print(R)
else:
    print(R1)
