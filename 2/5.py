import itertools

points = [(0, 1), (3, 5), (6, 1), (10, 6), (15, 3)]     # массив точек
all_combinations = list(itertools.combinations(points, 2))  # создаем всевозможные комбинации с помощью библиотеки, где в каждой паре по 2 элемента
all_length = []     # массив расстояний
for pair in all_combinations:
    all_length.append(((pair[0][0] - pair[1][0]) ** 2 + (pair[0][1] - pair[1][1]) ** 2) ** (1 / 2)) # считаем расстояние и добавляем в конец массива
for i in range(len(all_combinations)):
    print("Расстояние между точками: ", all_combinations[i], " - ", all_length[i])
index_of_min_length = all_length.index(min(all_length))     # ищем индекс минимального расстояния
print("Минимальное расстояние между точками: ",
      all_combinations[index_of_min_length], " - ", all_length[index_of_min_length])
