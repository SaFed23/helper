alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Просто алфавит
count_of_chars = 0
count_of_big_chars = 0

with open("2.txt") as file:
    string = file.readline()    # Считываем строку, т.к. это написано в условии

for char in string:     # Запускаем цикл по символам в строке
    if alphabet.find(char.lower()) != -1:   # Т.к. у нас алфавит состоит из маленьких букв, мы проверяем есть ли символ в нижнем регистре в алфавите. Тем самым мы будем работат только с буквами и все другие символы будут отброшены
        count_of_chars += 1     # Увеличиваем кол-во букв
        if alphabet.find(char) >= 33:   # Т.к. мы уже знаем, что работаем с буквой, мы проверяем есть ли эта буква в алфавите маленьких букв
            count_of_big_chars += 1     # Если буквы в алваите нет, значит это заглавная

print("Количество заглавных букв: ", count_of_big_chars)
print("Процентное содержание заглавных букв: ", count_of_big_chars * 100 / count_of_chars)
