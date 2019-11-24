from math import *
from tkinter import *


def func(x):
    return sin(x) / (x + 2)


root = Tk()

canv = Canvas(root, width=1200, height=600, bg="white")  # Создание окна
canv.create_line(600, 600, 600, 0, width=2, arrow=LAST)     # Создание вертикальной оси
canv.create_line(0, 300, 1200, 300, width=2, arrow=LAST)     # Создание горизонтальной оси

for i in range(-6, 6):
    canv.create_line((i * 100) + 600, -3 + 300, (i * 100) + 600, 3 + 300, width=0.5, fill='black')  # Рисуем штрихи на оси х
    canv.create_text((i * 100) + 610, 10 + 300, text=str(i * 1.0), fill="purple", font=("Helvectica", "10"))     # Ставим значения на оси х
    if i % 2 == 0:
        if i != 0:
            canv.create_line(-3 + 600, (i / 2 * 100) + 300, 3 + 600, (i / 2 * 100) + 300, width=0.5, fill='black')   # Рисуем штрихи на оси у
            canv.create_text(615, (i / 2 * 100) + 310, text=str(i / -2), fill="purple", font=("Helvectica", "10"))      # Ставим значения на оси у


for i in range(12001):
    x = -6 + i / 1000   # считаем значения х в зависимости от масштаба
    try:
        y = func(x) * 50    # считаем значения у в зависимости от масштаба
        canv.create_oval((x * 100 + 600), y + 300, ((x * 100) + 601), y + 301, fill='black')    # ставим точку
    except ZeroDivisionError:
        pass

canv.pack()
root.mainloop()
