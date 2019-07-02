n=int(input(""))
f=int(input(""))
if n < 0:
   print("no")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       f = f*i
   print(f)
