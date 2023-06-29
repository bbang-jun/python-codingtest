hour, min = input().split()
cookTime = int(input())
hour = int(hour)
min = int(min)

hour += cookTime//60
min += cookTime%60

if min >= 60:
    hour += 1
    min -=60
if hour >=24:
    hour -= 24

print(hour, min)