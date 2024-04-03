# -*- coding: utf-8 -*-
# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

""" ~~~ PARTIE DÉCLARATIVE ~~~ """

from tkinter import *

fenetre = Tk()
intro="Le jeu de la vie : des règles simples, une infinité de résolutions.\n\nLe jeu de la vie c’est 2 règles : Règle de survie, règle de naissance. \n\nAu début vous devrez choisir la taille du tableau puis la remplir comme vous le souhaitez, par la suite, vous verrez le développement des cellules*.\nA savoir que si une cellule* ne survie pas, elle meurt.\n*cellule = case pleine\nUne case est entourée de 8 autres cases (haut, droite, diagonales…), on fait son compte et on regarde comment évolue l’état de chaque case :\n\n\nRègle de survie : \nSi une cellule est entourée de plus d’1 cellule et de moins de 4 cellules, elle survie au prochain tour.\n\nRègle de naissance :\nSi une case vide est entourée de exactement 3 cases, alors elle sera vivante le tour d’après."

introduction = Label(fenetre, text=intro)


""" ~~~ PARTIE FONCTIONNELLE ~~~ """



""" ~~~ PARTIE EXECUTIVE ~~~ """

introduction.pack()

fenetre.mainloop()
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

class naissance:
    def __init__(self, voisines, case):
        self.voisines = voisines
        self.case = case
    def lookforvide(self, case):
