import random


k = int(input("Введите наименьшее число: "))
n = int(input("Введите наибольшее число: "))
arr = [random.randint(0, 100) for i in range(int(input("Введите количество элементов: ")))]
print(arr)
for num in arr:
    if k <= num <= n:
        print(num)
