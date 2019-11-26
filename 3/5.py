n = int(input("Введите размерность n: "))
m = int(input("Введите размерность m: "))

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
