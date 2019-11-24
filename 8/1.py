"""Все объяснения есть в методичке, поэтому комментарии не писал.
Я занимался переводом из python 2, на котором написано в методе, в python 3 и устранением некоторых неисправностей"""

from nltk.book import *


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count, total):
    return 100 * count / total


print("*************************")
print(text6)
print("*************************")
print(text1.concordance("monstrous"))
print("*************************")
print(text3.similar("monstrous"))
print("*************************")
print(text2.common_contexts(["monstrous", "very"]))
print("*************************")
print(len(text9))
print("*************************")
print(set(text8))
t8 = sorted(set(text8))
print(t8)
print(len(set(text8)))
print("*************************")
print(len(text5) / len(set(text5)))
print("*************************")
print(text4.count("smote"))
print("*************************")
print(lexical_diversity(text4))
print(percentage(text4.count("smote"), len(text4)))
print("*************************")
print(sent1, "\n", sent2)
print(len(sent1))
print(lexical_diversity(sent1))
print("*************************")
str1 = ["holly", "xmas", "bell", "tree"]
str2 = ["egg", "rabbit", "Easter", "chocolate"]
print(str1 + str2)
print(sent1 + sent7)
sent2.append("Something")
print(sent2)
print("*************************")
print(text5[10])
print(text2.index("some"))
print("*************************")
print(text6[16:167])
print("*************************")
print(sorted(text6))
s = ', '.join(['Hello', 'World!'])
print(s)
print(s.split(", "))
print("*************************")
fdist = FreqDist(text2)
print(fdist)
vocabulary = list(fdist.keys())
print(vocabulary[:50])
print(fdist['whale'])
print("*************************")
print(fdist.plot(50, cumulative=True))
print("*************************")
V = set(text5)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))
print("*************************")
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))
print("*************************")
print(text5.collocation_list())     # функция, которая в методе бьет ошибку, а эта просто возвращает список



