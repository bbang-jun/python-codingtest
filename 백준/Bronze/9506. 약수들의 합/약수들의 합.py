while True:
    n = int(input())
    if n == -1:
        break

    temp = 1
    divisor = []
    while n != temp:
        if n % temp == 0:
            divisor.append(temp)
        temp += 1

    hap = 0
    for i in range(len(divisor)):
        hap += int(divisor[i])

    if n == hap:
        print(str(n) + " = ", end="")
        for i in range(len(divisor)):
            if i == len(divisor) - 1:
                print(divisor[i])
            else:
                print(str(divisor[i]) + " + ", end="")
    else:
        print(str(n) + " is NOT perfect.")