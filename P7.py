numb1=int(input())
numb2=1
while(numb2<=numb1 and numb2*2<=numb1):
    numb2=numb2*2
if(numb2==numb1):
    print("0")
else:    
    print(numb1-numb2)
