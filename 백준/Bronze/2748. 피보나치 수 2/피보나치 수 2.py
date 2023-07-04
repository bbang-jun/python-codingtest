n = int(input())

n_1 = 1
n_2 = 1
num = 0

if n == 0:
  print(0)
elif n == 1:
  print(1)
elif n == 2:
  print(1)
else:
  for _ in range(n - 2):
    num = n_1 + n_2
    n_2 = n_1
    n_1 = num
  print(num)
