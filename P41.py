A,B=input().split()
A=int(A)
B=int(B)
s=''
u=2
if(A+B<=3):
    for i in range(0,A+B):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,A+B):
        if(i==u):
            s=s+'0'
            if(u==B):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif A==1 and B==2: 
     print("011")
else:
    print(s)
