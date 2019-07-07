vjs,vk=map(int,input().split())
ls=list(map(int,input().split()))
vjs=[]
ls.insert(0,0)
for a in range(vk):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for b in range(cc,dd+1):         
         sumup^=ls[b]     
     vjs.append(sumup)
for c in vjs:
    print(c)
