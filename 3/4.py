n = int(input("Введите размерность: "))
matrix = []
for i in range(n):
    line = [int(input("Введите элемент: "))for j in range(n)]
    matrix.append(line)
print("Исходная матрица: ", matrix)

new_matrix = []
for line in matrix[::-1]:
    new_matrix.append(line[::-1])

print("Обратная матрица: ", new_matrix)

