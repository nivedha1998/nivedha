s=input()
t=input()
for i in range(len(s)):
    n=ord(s[i])
    r=ord(t[i])
    l=((n-96)+(r-96))
    if(l > 26)and(l%26!=0):
        l=(((n-96)+(r-96))%26)+96
        print(chr(l),end='')
    elif(l%26==0):
        l=122
        print(chr(l),end='')
    else:
        l=(((n-96)+(r-96))+96)
        print(chr(l),end='')
