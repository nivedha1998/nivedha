s=input()
fin=''
for k in range(0,len(s)-1,2):
  if int(s[k+1])%2==0:
    fin+=s[k]*int(s[k+1])
  else:
    fin+=s[k]+s[k+1]
print(fin)
