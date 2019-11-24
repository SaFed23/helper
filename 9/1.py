import nltk

with open("1_text1.txt") as file1:
    text1 = nltk.word_tokenize(file1.readline())    # Разбивает слова на токены

with open("1_text2.txt") as file2:
    text2 = nltk.word_tokenize(file2.readline())

print("Коэффициент разнообразия художественного текста: ", len(set(text1)) / len(text1))    # set - это множество, т.е. уникальные элементы
print("Коэффициент разнообразия научного текста: ", len(set(text2)) / len(text2))
