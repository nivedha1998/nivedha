y,y2 = map(int,input().split())
m1 = list(map(int,input().split()))
amount = int(input())
total = (sum(m1)-m1[y2])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
