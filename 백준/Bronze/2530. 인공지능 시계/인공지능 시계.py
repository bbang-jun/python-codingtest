A, B, C = input().split()
D = int(input())
A = int(A)
B = int(B)
C = int(C)

C += D % 60
D = D // 60

if C >= 60:
    B += 1
    C -= 60

B += D % 60
D = D // 60
if B >= 60:
    A += 1
    B -= 60

A += D % 24


if A>=24:
    A-=24

print(A, B, C)