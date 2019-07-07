ax,ay=map(int,input().split())
mh=list(map(int,input().split()))
mh.sort()
mh.reverse()
ah=ay
Z=0
for i in mh:
    if(ah>=i):
        no=int(ah/i)
        Z=Z+no
        ah=ah-no*i
    if ah==0:
        break
if(ah==0):
   print(Z)
else:
   print("it is not posible to select coins ",S)  
