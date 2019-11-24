from math import *
from tkinter import *


def func(x):
    return x ** 3 - 7


root = Tk()

canv = Canvas(root, width=420, height=600, bg="white")  # Создание окна
canv.create_line(210, 600, 210, 0, width=2, arrow=LAST)     # Создание вертикальной оси
canv.create_line(0, 300, 420, 300, width=2, arrow=LAST)     # Создание горизонтальной оси

for i in range(-15, 15):
    if i % 3 == 0:
        canv.create_line(-3 + 210, (i * 20) + 300, 3 + 210, (i * 20) + 300, width=0.5, fill='black')    # Рисуем штрихи на оси у
        canv.create_text(230, (i * 20) + 310, text=str(i * -1.0), fill="purple", font=("Helvectica", "10"))     # Ставим значения на оси у
        if i != 0:
            canv.create_line((i * 14) + 210, -3 + 300, (i * 14) + 210, 3 + 300, width=0.5, fill='black')    # Рисуем штрихи на оси у
            canv.create_text((i * 14) + 220, 315, text=str(i / 3), fill="purple", font=("Helvectica", "10"))    # Ставим значения на оси х


for i in range(10001):
    x = (-5 + i / 1000) * -1    # считаем значения х в зависимости от масштаба (умножаем на -1, т.к. график получается отзеркаленым относительно оси у
    try:
        y = func(-x) * 20 + 600     # считаем значения у в зависимости от масштаба
        canv.create_oval((x * 84) + 210, y, (x * 84) + 211, y + 1, fill='black')
    except ZeroDivisionError:
        pass

canv.pack()
root.mainloop()
