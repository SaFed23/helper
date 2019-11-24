key = "супинкаялюдм"
string = "привет, мир."


def encryption(s):    # Объявление функции
    new_string = ""
    new_key = ""
    i = 0
    while len(new_key) < len(s):
        new_key += key[i]
        i += 1
        i %= len(key)
    for i in range(len(s)):
        code = ord(s[i]) + ord(new_key[i])
        if code > 1103:
            code -= 1103
        new_string += chr(code)
    return new_string


def decryption(s):
    new_string = ""
    new_key = ""
    i = 0
    while len(new_key) < len(s):
        new_key += key[i]
        i += 1
        i %= len(key)
    for i in range(len(s)):
        code = ord(s[i]) - ord(new_key[i])
        if code < 0:
            code += 1103
        new_string += chr(code)
    return new_string


s = encryption(string)
print(s)
print(decryption(s))
