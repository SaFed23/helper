from math import *
from tkinter import *


root = Tk()

canv = Canvas(root, width=600, height=600, bg="white")  # Создание окна
canv.create_rectangle(10, 200, 590, 300, fill="white")
canv.create_rectangle(10, 300, 590, 400, fill="blue")
canv.create_rectangle(10, 400, 590, 500, fill="red")

canv.pack()
root.mainloop()
