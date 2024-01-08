decimal = 12345
binary = []
prints = ""

if __name__ == '__main__':
    while True:
        if decimal == 0:
            break
        if decimal % 2 == 1:
            binary.append(str(1))
        elif decimal % 2 == 0:
            binary.append(str(0))
        decimal = decimal // 2

    while binary:
        prints += binary.pop()

    print(prints)