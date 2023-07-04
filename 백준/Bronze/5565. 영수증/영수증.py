total = int(input())
price = 0

for _ in range(9):
  a = int(input())
  price += a

print(total - price)