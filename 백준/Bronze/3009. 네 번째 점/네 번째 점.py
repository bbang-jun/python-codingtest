pointX = []
pointY = []
for i in range(3):
    a, b = map(int, input().split())
    pointX.append(a)
    pointY.append(b)

for j in range(3):
    if pointX.count(pointX[j]) == 1:
        x = pointX[j]
    if pointY.count(pointY[j]) == 1:
        y = pointY[j]

print(x, y)