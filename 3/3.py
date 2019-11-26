import random


k = int(input("Введите наименьший индекс: "))
n = int(input("Введите наибольший индекс: "))
arr = [random.randint(0, 100) for i in range(int(input("Введите количество элементов: ")))]
print(arr)
for i in range(len(arr)):
    if k <= i <= n:
        print(arr[i])
