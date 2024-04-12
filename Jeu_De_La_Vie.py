# -*- coding: utf-8 -*-
# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

""" ~~~ PARTIE DÉCLARATIVE ~~~ """

from tkinter import *

#dimensions des pixels et du canva
couleur = 'pink'
nb_pixels_longueur = 10
nb_pixels_largeur = 8
longueur_canva = nb_pixels_longueur * 50
largeur_canva = nb_pixels_largeur * 50

""" ~~~ PARTIE FONCTIONNELLE ~~~ """

class Tableau:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def creation_tableau(longueur, largeur):
        # creer le quadrillage
        tableau_de_tableaux = []
        for i in range(largeur):
            ligne = []
            for j in range(longueur):
                ligne.append(0)
            tableau_de_tableaux.append(ligne)

        # Afficher le quadrillage
        for ligne in tableau_de_tableaux:
            print(ligne)
        return tableau_de_tableaux

class Vide:
    def __init__(self, matrice, cox, coy):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
    def lookfornaissance(self, matrice, cox, coy):
        if self.matrice[self.cox][self.coy] == 0:
            cmpt = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if self.matrice[cox+i][coy+j] == 1:
                        cmpt += 1
            if cmpt == 3:
                return 1
            else:
                return 0
        else:
            return 1



""" ~~~ PARTIE EXECUTIVE ~~~ """

#fenetre 1 : explication des règles du jeu.
fenetre1 = Tk()
intro="Le jeu de la vie : des règles simples, une infinité de résolutions.\n\nLe jeu de la vie c’est 2 règles : Règle de survie, règle de naissance. \n\nAu début vous devrez choisir la taille du tableau puis la remplir comme vous le souhaitez, par la suite, vous verrez le développement des cellules*.\nA savoir que si une cellule* ne survie pas, elle meurt.\n*cellule = case pleine\n\n\nRègle de survie : \nSi une cellule est entourée de plus d’1 cellule et de moins de 4 cellules, elle survie au prochain tour.\n\nRègle de naissance :\nSi une case vide est entourée de exactement 3 cases, alors elle sera vivante le tour d’après."

bouton=Button(fenetre1, text="Compris", command=fenetre1.quit)
bouton.pack(side=BOTTOM, padx=150, pady=20)
bouton.pack()

introduction = Label(fenetre1, text=intro)
introduction.pack()

fenetre1.mainloop()

#fenêtre 2 : interface graphique du jeu de la vie.
fenetre2 = Tk()



# grid
fenetre2.geometry("400x400")
x = 0
i = 0
j = 0

tab = [[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1]]

def carre_noir(x, y):
    can1 = Canvas(fenetre2, height=40, width=40, bg="black")
    can1.grid(column=x, row=y)


def carre_blanc(x, y):
    can1 = Canvas(fenetre2, height=40, width=40, bg="white")
    can1.grid(column=x, row=y)



while j <= 6:
    while i < 6:

        if tab[j][i]== 1:
            carre_noir(j, x)
        else:
            carre_blanc(j, x)
        x += 1
        i += 1

    i = 0
    x = 0
    y = 0
    j += 1

#remplacer la couleur d'une case : (penser à changer la grille aussi !!)
'''can1 = Canvas(fen1, height=40, width=40, bg="white")
can1.grid(column=1, row=1)'''



# bouton de sortie

bouton=Button(fenetre2, text="Fermer", command=fenetre2.quit)
bouton.grid(column=3, row=11)

bouton=Button(fenetre2, text="Retour", command=fenetre2.quit)
bouton.grid(column=2, row=10)

bouton=Button(fenetre2, text="Avance", command=fenetre2.quit)
bouton.grid(column=4, row=10)

fenetre2.mainloop()