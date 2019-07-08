nn,mm=map(eval,input().split())
aut=[]
for k in range(nn):
  aut.append(list(map(eval,input().split())))
pos=[]
out=[]
temp_out=[]
tt=[]
k=0
j=0
out.append(aut[k][j])
pos.append([k,j])
while [nn-1,mm-1] not in pos:
  k=0
  for x in pos:
    if x[0]+1<nn and x[1]+1<mm:
      temp_out.append(aut[x[0]+1][x[1]]+out[k])
      temp_out.append(aut[x[0]][x[1]+1]+out[k])
      tt.append([x[0]+1,x[1]])
      tt.append([x[0],x[1]+1])
    elif x[0]+1<nn:
      temp_out.append(aut[x[0]+1][x[1]]+out[k])
      tt.append([x[0]+1,x[1]])
    elif x[1]+1<mm:
      temp_out.append(aut[x[0]][x[1]+1]+out[k])
      tt.append([x[0],x[1]+1])
    k+=1
  pos=tt
  tt=[]
  out=temp_out
  temp_out=[]
print(max(out))
