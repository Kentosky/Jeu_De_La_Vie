# -*- coding: utf-8 -*-
# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

""" ~~~ PARTIE DÉCLARATIVE ~~~ """

from tkinter import *

# --- La bibliothèque permettant de faire les graphismes --- #
""" ~~~ PARTIE FONCTIONNELLE ~~~ """

class Tableau:
    """ Classe qui permet de créer une liste de listes qui sera ensuite interprété comme toutes les cases du jeu de la vie. """
    def __init__(self, longueur, largeur):      # Initialisation
        self.longueur = longueur
        self.largeur = largeur
    def creation_tableau(self):                 #fonction principale permettant de créer la liste de liste
        # creer le quadrillage
        tableau_de_tableaux = []
        for i in range(self.largeur):           #la liste de listes fera une largeur de la variable largeur
            ligne = []
            for j in range(self.longueur):      #la liste de listes fera une longueur de la variable longueur
                ligne.append(0)
            tableau_de_tableaux.append(ligne)

        # Afficher le quadrillage
        for ligne in tableau_de_tableaux:       #ici, on affiche la liste de listes pour la vérification
            print(ligne)
        return tableau_de_tableaux

class Cellule:
    def __init__(self, matrice, coy, cox):      # dans cet ordre car on cree les colones avant les lignes
        self.cox = cox                          # coordonnée x
        self.coy = coy                          # coordonnée y
        self.matrice = matrice                  # matrice
        # on créé une matrice temporaire pour pouvoir faire tous les déplacements sans risquer un effet domino
        self.temp_matrice = []
        for row in matrice:
            self.temp_matrice.append(row[:])

    def regle(self):
        # on gère d'abord le cas où la cellule est collé a un coté du quadrillage
        left = top = right_or = bottom_or = 0
        right = len(self.matrice[0])
        bottom = len(self.matrice)

        if self.cox == left:
            left += 1
        if self.cox == right:
            right_or += 1
        if self.coy == top:
            top += 1
        if self.coy == bottom:
            bottom_or += 1

        # on gère maintenant la survie de la cellule
        if self.matrice[self.coy][self.cox] == 1:                       # 1er cas: la cellule est vivante
            cmptS = 0                                                   # compteur de voisins
            for i in range(top - 1, 2 - bottom_or):                     # on regarde autour de la cellule
                for j in range(left - 1, 2 - right_or):                 #               |
                    if self.matrice[self.coy + i][self.cox + j] == 1:   # si une voisine est vivante
                        cmptS += 1                                      # on incrémente le compteur de voisins

            if cmptS == 3 or cmptS == 4:                                # si la cellule a 2 ou 3 voisines (compteur=3 ou 4 car elle se compte elle-même)
                return self.matrice                                     # rien ne se passe, la cellule reste en vie
            else:
                self.temp_matrice[self.coy][self.cox] = 0               # sinon la cellule meurt, on modifie son état
                return self.temp_matrice
        else:                                                           # 2eme cas:la cellule est morte
            cmptN = 0                                                   # compteur de voisins
            for i in range(top - 1, 2 - bottom_or, 1):                  # on regarde autour de la voisine
                for j in range(left - 1, 2 - right_or, 1):              #               |
                    if self.matrice[self.coy + i][self.cox + j] == 1:   # si une voisine est vivante
                        cmptN += 1                                      # on incrémente le compteur
            if cmptN == 4:                                              # si la cellule a 3 voisines (compteur=4 car elle se compte elle-même)
                self.temp_matrice[self.coy][self.cox] = 1               # la cellule meurt, on modifie son état
                return self.temp_matrice
            else:
                return self.matrice                                     # sinon rien ne se passe, la cellule reste morte

    def appliquer_modifications(self): # Cette fonction applique les modifications de la matrice temporaire dans la matrice de base
        for row in self.temp_matrice:
            self.matrice.append(row[:])
        return self.matrice



""" ~~~ PARTIE EXECUTIVE ~~~ """

#fenetre 1 : explications des règles du jeu.
fenetre1 = Tk()
intro="Le jeu de la vie : des règles simples, une infinité de résolutions.\n\nLe jeu de la vie c’est 2 règles : Règle de survie, règle de naissance. \n\nAu début vous devrez choisir la taille du tableau puis la remplir comme vous le souhaitez, par la suite, vous verrez le développement des cellules*.\nA savoir que si une cellule* ne survie pas, elle meurt.\n*cellule = case pleine\n\n\nRègle de survie : \nSi une cellule est entourée de plus d’1 cellule et de moins de 4 cellules, elle survie au prochain tour.\n\nRègle de naissance :\nSi une case vide est entourée de exactement 3 cases, alors elle sera vivante le tour d’après."

#création d'un bouton pour passer à la fenêtre suivante
bouton=Button(fenetre1, text="Compris", command=fenetre1.quit)
bouton.pack(side=BOTTOM, padx=150, pady=20)
bouton.pack()

introduction = Label(fenetre1, text=intro)
introduction.pack()

fenetre1.mainloop()


#fenêtre 2 : choix des pixels colorés sous forme de boutons
fenetre2 = Tk()

# grille
fenetre2.geometry("800x700")
x = 0
i = 0
j = 0

#matrice temporaire pour test
tab1 = Tableau(10, 10)
tab = tab1.creation_tableau()
print(tab1.creation_tableau())

#quand un bouton est cliqué la couleur change
def changer_couleur(bouton, x, y):
    couleur_actuelle = bouton["bg"]
    nouvelle_couleur = "white" if couleur_actuelle =="black" else "black"
    bouton.config(bg=nouvelle_couleur)
    if nouvelle_couleur == "white" :
        tab[x][y] = 0
    else :
        tab[x][y] = 1

#mise en place des boutons représentant les cellules
def bouton_carre_noir(x, y):
    bouton = Button(fenetre2, height=3, width=6, bg="black", command=lambda ligne=x, colonne = y: changer_couleur(bouton, x, y))
    bouton.grid(column=x, row=y)

def bouton_carre_blanc(x, y):
    bouton = Button(fenetre2, height=3, width=6, bg="white", command=lambda ligne=x, colonne = y: changer_couleur(bouton, x, y))
    bouton.grid(column=x, row=y)

#affichage de la grille
while j <= len(tab)-1:
    while i < len(tab[1])-1:

        if tab[j][i]==1:
            bouton_carre_noir(j, x)
        else:
            bouton_carre_blanc(j, x)
        x += 1
        i += 1

    i = 0
    x = 0
    y = 0
    j += 1

# bouton de sortie
bouton=Button(fenetre2, text="Fermer", command=fenetre2.quit)
bouton.grid(column=3, row=11)

bouton=Button(fenetre2, text="Retour")
bouton.grid(column=2, row=10)

bouton=Button(fenetre2, text="Avance")
bouton.grid(column=4, row=10)

fenetre2.mainloop()

#fenêtre 3 : affichage interface graphique du jeu de la vie.
'''
Dans cet affichage la couleur des cellules n'est plus modifiable, 
à chaque modification de matrice un nouveau caneva sera généré
'''

fenetre3 = Tk()

# grid
fenetre3.geometry("800x700")
x = 0
i = 0
j = 0

#génération des cellules noires et blanches
def carre_noir(x, y):
    can1 = Canvas(fenetre3, height=50, width=50, bg="black")
    can1.grid(column=x, row=y)

def carre_blanc(x, y):
    can1 = Canvas(fenetre3, height=50, width=50, bg="white")
    can1.grid(column=x, row=y)

#génération de la grille
while j <= len(tab)-1:
    while i < len(tab[1])-1:

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

# bouton de sortie
bouton=Button(fenetre3, text="Fermer", command=fenetre3.quit)
bouton.grid(column=3, row=11)

bouton=Button(fenetre3, text="Retour", command=fenetre3.quit)
bouton.grid(column=2, row=10)

bouton=Button(fenetre3, text="Avance", command=fenetre3.quit)
bouton.grid(column=4, row=10)

fenetre3.mainloop()