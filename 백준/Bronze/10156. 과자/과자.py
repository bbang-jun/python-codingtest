K, N, M = map(int, input().split())
price = K*N

if M >= price:
    print("0")
else:
    print(price - M)