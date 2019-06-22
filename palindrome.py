N=int(input("Enter number:"))
temp=N
r=0
while(N<=1000):
    dig=N%10
    r=r*10+dig
    N=N//10
if(temp==r):
    print("Yes")
else:
    print("No")
