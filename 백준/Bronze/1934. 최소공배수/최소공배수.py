def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

testCase = int(input())

for i in range(testCase):
    a, b = map(int, input().split())
    print(lcm(a, b))
