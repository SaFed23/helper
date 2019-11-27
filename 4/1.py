import time
import random

print("Первая задача\n\n")
n = int(input("Введите количество элементов: "))
for count in range(1, 6):
    new_array = []
    start = time.time()
    arr = [random.randint(0, 100) for i in range(n)]
    print("Исходный массив: ", arr)
    i = 0
    while i < len(arr):
        if i % 3 == 0:
            new_array.append(arr[i])
        i += 1
    print("Результат: ", new_array)
    print("Время выполнения " + str(count) + ": ", time.time() - start)


print("Вторая задача\n\n")
n = int(input("Введите размерность n: "))
m = int(input("Введите размерность m: "))

for count in range(1, 6):
    start = time.time()

    last_num = 3
    curr_num = 5

    matrix = []

    for i in range(n):
        line = []
        for j in range(m):
            if i == 0 and j == 0:
                line.append(last_num)
            elif i == 0 and j == 1:
                line.append(curr_num)
            else:
                line.append((last_num + curr_num) / 2)
                last_num = curr_num
                curr_num = line[-1]
        matrix.append(line)

    for line in matrix:
        print(" ".join(map(str, line)))

    print("Время выполнения " + str(count) + ": ", time.time() - start)


