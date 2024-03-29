import re


square = [["с", "у", "п", "и", "н", "к"],   # Это массив для шифрования, составлен по заданию
          ["а", "я", "л", "ю", "д", "м"],
          ["б", "в", "г", "е", "ё", "ж"],
          ["з", "й", "о", "р", "т", "ф"],
          ["х", "ц", "ч", "ш", "щ", "ъ"],
          ["ы", "ь", "э", ",", ".", " "]]

string = "привет, мир."


def search_in_square(char):
    for i in range(len(square)):
        for j in range(len(square[0])):
            if square[i][j] == char:
                return i + 1, j + 1


def encryption(s):    # Объявление функции
    """Функция для шифрования
    join - объединение элементов массива через соответствующую строку;
    map - функция для итерирования, возвращает итератор, первый аргумент - это ссылка на функцию, второй - итерируемый объект"""
    array = []
    for char in s.lower():
        array.append("(" + ", ".join(map(str, search_in_square(char))) + ")")
    return "".join(array)


def decryption(s):
    """Функия для расшифровки
    split - разбивает строку через соответствующий символ;
    библиотека re - для регулярных выражений (это есть в примере в методе, значит пользоваться можно;
    r - обозначает, что это чистая строка, т.е. все симолы считываются отдельно
    lambda x: int(x) - 1 - это лямбда функия, тип сокращенная до двоеночия х - это переменная, которую функция принимает,
    после двоеточия мы описываем, что мы делаем (приводим к целому типу и отнимаем 1, чтоб вернуться к индексам в матрице"""
    new_string = ""
    arr = s.split(")(")
    for el in arr:
        line = list(map(lambda x: int(x) - 1, re.findall(r"\d", el)))  # re.findall(r"\d", el) мы находим все цифры в el
        new_string += square[line[0]][line[1]]
    return new_string


s = encryption(string)
print(decryption(s))
