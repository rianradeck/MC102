from decimal import Decimal

a = Decimal(input())

A = int(a // 10)
a -= A * 10
B = int(a // 1)
a -= B
C = int(a * 10)
# print(a, C, Decimal(C) / 10)
a -= Decimal(C) / 10
# print(a)
D = int(a * 100)
# print(D)

print("R$ ", D, C, ".", B, A, sep="")