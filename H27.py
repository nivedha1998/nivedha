S=input()
a=len(S)
b=S[::-1]
if S==b:
  print(S[:a-1])
else:
  print(S)
