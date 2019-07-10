I=int(input())
while(I>0):
    j=0
    while(j<I):
        if (j==(I-1)):
            print("1")
        else:
            print("1",end=" ")
        j+=1
    I-=1
