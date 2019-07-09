n = int(input())
def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
if n <= 2:
  print(n)
else:
  print((n+(factorial(n)//(factorial(n-2)*factorial(2))))//2)
