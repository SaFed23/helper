import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
e = int(input("Введите e: "))
f = int(input("Введите f: "))

fac_a = math.factorial(a)
fac_b = math.factorial(b)
fac_c = math.factorial(c)
fac_d = math.factorial(d)
fac_e = math.factorial(e)

if fac_a > f:
    print(a)
if fac_b > f:
    print(b)
if fac_c > f:
    print(c)
if fac_d > f:
    print(d)
if fac_e > f:
    print(e)
