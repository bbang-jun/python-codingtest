odd = []
total = 0
for _ in range(7):
  n = int(input())
  if n % 2 == 1:
    odd.append(n)
    total += n
  else:
    continue

if len(odd) == 0:
  print(-1)
else:
  odd.sort()
  print(total)
  print(odd[0])