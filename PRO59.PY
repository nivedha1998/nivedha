x1,y1=map(str,input().split("|"))
c=input()
if len(x1)>len(y1):
  if len(x1)==len(y1+c):
    print(x1+"|"+y1+c)
elif len(x1)<len(y1):
  if len(x1+c)==len(y1):
    print(x1+c+"|"+y1)
elif len(x1)==len(y1) and len(c)>1 or (len(y1)or len(x1))==0:
  print("Impossible")
