num = int(input())

while num > 1:
    for i in range(1, num+1):
        if num % i == 0 and i != 1:
            print(i)
            num = num // i
            break