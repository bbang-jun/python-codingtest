result = 0
zero = 0
one = 0

strings = list(map(int, input()))

for i in range(0, len(strings)-1):
    if strings[i] == strings[i+1]:
        continue
    else:
        if strings[i] == 0:
            zero+=1
        else:
            one+=1

if strings[-1] == 0:
    zero+=1
else:
    one+=1

if zero <= one:
    print(zero)
else:
    print(one)