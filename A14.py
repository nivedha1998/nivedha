x=0;
def removal(string):
  vowels=('a','e','i','o','u')
  for x in string.lower():
   if x in vowels:
      string=string.replace(x,"")
  print(string)
n=list(map(int,input()))
string = input()
removal(string[::-1])      
