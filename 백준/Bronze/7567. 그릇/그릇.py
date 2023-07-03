plate = input()
height = 10
for i in range(len(plate) - 1):
    if plate[i] != plate[i+1]:
        height += 10
    else:
        height += 5

print(height)