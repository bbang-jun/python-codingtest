M = int(input())
N = int(input())

temp = 1
hap = 0
min = 0
first = True
while temp <= N:
  if M <= temp**2 <= N:
    if first == True:
      min = temp**2
      first = False
    hap += temp**2
  temp += 1

if hap == 0:
  print(-1)
else:
  print(hap)
  print(min)