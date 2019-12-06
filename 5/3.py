arr = []
with open("1.txt") as file:     # Блок служит для автоматического открытия и закрытия файла после окончания работы
    for line in file.readlines():   # Считываем все строки
        num = int(line.replace("\n", ""))   # Т.к. строка заканчивается на '\n' необходимо этот символ удалить и привести строку к целому типу
        if num % 2 == 0:
            arr.append(str(num))
new_arr = arr[::-1]
with open("3.txt", "w") as file:
    file.write("\n".join(new_arr))
