key = 19
string = "привет, мир!"


def encryption(s):    # Объявление функции
    s = s.lower()
    new_string = ""
    for i in range(len(s)):
        code = ord(s[i]) + key    # Прибавляем ключ для поиска нового элемента
        if code >= 1103:   # Если ключ вышел за рамки то, ...
            code -= 1103
        new_string += chr(code)
    return new_string


def decryption(s):
    new_string = ""
    for i in range(len(s)):
        code = ord(s[i]) - key    # Для расшифровк ключ отнимаем
        if code < 0:    # Если индекс меньше 0 то, ...
            code += 1103  # ... прибавляем длину массива
        new_string += chr(code)
    return new_string


s = encryption(string)
print(s)
print(decryption(s))
