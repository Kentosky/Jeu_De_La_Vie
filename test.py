# !/usr/bin/python
from tkinter import *

fenetre2 = Tk()
fenetre2.title("Damier")
fenetre2.geometry("400x400")
x = 0
i = 0
j = 0

tab = [[0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1],
       [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1]]


def carre_noir(x, y):
    can1 = Canvas(fenetre2, height=40, width=40, bg="black")
    can1.grid(column=x, row=y)


def carre_blanc(x, y):
    can1 = Canvas(fenetre2, height=40, width=40, bg="white")
    can1.grid(column=x, row=y)


while j <= 6:
    while i < 6:

        if tab[j][i] == 1:
            carre_noir(j, x)
        else:
            carre_blanc(j, x)
        x += 1
        i += 1

    i = 0
    x = 0
    y = 0
    j += 1

# remplacer la couleur d'une case : (penser à changer la grille aussi !!)
'''can1 = Canvas(fen1, height=40, width=40, bg="white")
can1.grid(column=1, row=1)'''

fenetre2.mainloop()
