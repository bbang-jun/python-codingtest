case = int(input())

for i in range(case):
    char = list(map(str, input().split()))
    answer = 0
    for j in range(len(char)):
        if j == 0:
            answer = float(char[j])
        else:
            if char[j] == "@":
                answer *= 3
            elif char[j] == "%":
                answer += 5
            elif char[j] == "#":
                answer -= 7
    print("%0.2f" %answer)
