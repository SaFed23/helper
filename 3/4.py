n = int(input("Введите размерность: "))
matrix = []
for i in range(n):
    line = []
    for num in input("Введите строку: ").split(" "):
        line.append(num)
    matrix.append(line)

new_matrix = []
for line in matrix[::-1]:
    new_matrix.append(line[::-1])

print("Обратная матрица: ")
for line in new_matrix:
    print(" ".join(line))

