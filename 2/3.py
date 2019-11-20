a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))

if b < a > c:
    print(a ** 2 == b ** 2 + c ** 2)
elif a < b > c:
    print(b ** 2 == a ** 2 + c ** 2)
elif a < c > b:
    print(c ** 2 == a ** 2 + b ** 2)
else:
    print(False)
