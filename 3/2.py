arr_of_days = ["Среда", "Четверг", "Пятница", "Суббота", "Воскресенье", "Понедельник", "Вторник"]
number = int(input("Введите чило: "))
print(arr_of_days[(number % 7) - 1])
