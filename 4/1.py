import time
import random


start = time.time()
arr = [random.randint(0, 100) for i in range(int(input("Введите количество элементов: ")))]
print(arr)
i = 0
while i < len(arr):
    if i % 3 == 0:
        print(arr[i])
    i += 1
print("Время выполнения: ", time.time() - start)
