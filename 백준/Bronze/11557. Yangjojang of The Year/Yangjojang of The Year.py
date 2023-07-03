T = int(input())

for _ in range(T):
    N = int(input())

    mostDrink = 0
    mostSchool = ""
    for i in range(N):
        S, L = map(str, input().split())
        L = int(L)
        if mostDrink < L:
            mostDrink = L
            mostSchool = S
    print(mostSchool)