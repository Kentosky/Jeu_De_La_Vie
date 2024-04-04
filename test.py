# !/usr/bin/python
from tkinter import *

fen1 = Tk()
fen1.title("Damier")
fen1.geometry("400x400")
x = 0
i = 0
j = 0

tab = [[0, '*', 0, '*', '*', '*'], [0, '*', 0, '*', '*', '*'],[0, '*', 0, '*', '*', '*'],[0, '*', 0, '*', '*', '*'],[0, '*', 0, '*', '*', '*'],[0, '*', 0, '*', '*', '*'],[0, '*', 0, '*', '*', '*']]

def carre_noir(x, y):
    can1 = Canvas(fen1, height=40, width=40, bg="black")
    can1.grid(column=x, row=y)


def carre_blanc(x, y):
    can1 = Canvas(fen1, height=40, width=40, bg="white")
    can1.grid(column=x, row=y)


while j <= 6:
    while i < 6:

        if tab[j][i]== '*':
            carre_noir(j, x)
        else:
            carre_blanc(j, x)
        x += 1
        i += 1

    i = 0
    x = 0
    y = 0
    j += 1

fen1.mainloop()