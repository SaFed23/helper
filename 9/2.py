"""Я взял на русском и на английском. Думаю, что то, что написано в методе в скобках на английском и немецком
 - это просто пример"""

import nltk


def count_of_words_with_1(text):        # Поиск слов с частотой 1
    count = 0
    for word in set(text):
        if text.count(word) == 1:
            count += 1
    return count


def count_of_words_with_more_or_equal_10(text):     # Поиск слов с частотой более или равно10
    count = 0
    for word in set(text):
        if text.count(word) >= 10:
            count += 1
    return count


with open("2_text1.txt") as file1:
    english_text = nltk.word_tokenize(file1.read())

with open("2_text2.txt") as file2:
    russian_text = nltk.word_tokenize(file2.read())

"""Анализируем на 100 словах, как написано в методичке"""
print("Коэффициент разнообразия английского текста: ", len(set(english_text[:100])) / len(english_text[:100]))  # [:100] - это срез означает, что мы берем первых 100 элементов
print("Коэффициент разнообразия русского текста: ", len(set(russian_text[:100])) / len(russian_text[:100]))

"""Анализируем на всем тексте для полноты картины"""
print("Коэффициент синтаксической сложности английского текста:", 1 - (english_text.count(".") / len(english_text)))
print("Коэффициент синтаксической сложности русского текста:", 1 - (russian_text.count(".") / len(russian_text)))

"""Анализируем на 100 словах, как написано в методичке"""
print("Индекс исключительности английского текста:", count_of_words_with_1(english_text[:100]) /
      len(english_text[:100]))
print("Индекс исключительности сложности русского текста:", count_of_words_with_1(russian_text[:100]) /
      len(russian_text[:100]))

"""Анализируем на всем тексте для полноты картины"""
print("Индекс концентрации английского текста:", count_of_words_with_more_or_equal_10(english_text) /
      len(english_text))
print("Индекс концентрации сложности русского текста:", count_of_words_with_more_or_equal_10(russian_text) /
      len(russian_text))

functors_pos_english = {'IN', 'СС'}     # IN - предлог, CC - союз для английского
functors_pos_russian = {'PR', 'CONJ'}    # тоже самое только для русского

"""Анализируем на всем тексте для полноты картины"""

"""
[word for word, pos in nltk.pos_tag(english_text, lang='eng') if pos in functors_pos_english] - генератор, был в предыдущих лабах,
но этот с условием
"""
print("Коэффициент связности речи английского текста:",
      len([word for word, pos in nltk.pos_tag(english_text, lang='eng') if pos in functors_pos_english]) /
      (3 * english_text.count(".")))
print("Коэффициент связности речи русского текста:",
      len([word for word, pos in nltk.pos_tag(russian_text, lang='rus') if pos in functors_pos_russian]) /
      (3 * russian_text.count(".")))
