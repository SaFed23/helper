import random


arr = [random.randint(0, 100) for i in range(int(input("Введите количество элементов: ")))]     # это называется генератором. помогает создавать массивы
print(arr)
i = 0
while i < len(arr):
    if i % 3 == 0:
        print(arr[i])
    i += 1
