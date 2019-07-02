n = int(input(""))
if n > 1:
    for i in range(2, n // 2):
      if (n % i) == 0:
       print(n," no not a prime number")
      else:
       print(n,"yes it is a prime number")
else:
 print(n," no not a prime number")
