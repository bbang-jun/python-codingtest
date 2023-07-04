n = int(input())

for _ in range(n):
  p = int(input())
  mostPrice = 0
  mostPlayer = ""
  for _ in range(p):
    price, player = map(str, input().split())
    price = int(price)
    if mostPrice < price:
      mostPrice = price
      mostPlayer = player
  print(mostPlayer)