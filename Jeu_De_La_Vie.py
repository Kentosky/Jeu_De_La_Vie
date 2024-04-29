# -*- coding: utf-8 -*-
# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

""" ~~~ PARTIE DÉCLARATIVE ~~~ """

from tkinter import *


""" ~~~ PARTIE FONCTIONNELLE ~~~ """

class Tableau:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def creation_tableau(self):
        # creer le quadrillage
        tableau_de_tableaux = []
        for i in range(self.largeur):
            ligne = []
            for j in range(self.longueur):
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
        # on créé une matrice temporaire pour pouvoir faire tous les déplacements sans risquer un effet domino
        self.temp_matrice = []
        for row in matrice:
            self.temp_matrice.append(row[:])
    def lookfornaissance(self):

        left = 0
        top = 0
        cmpt = 0
        bottom_OOR = 0
        right_OOR = 0

        right = len(self.matrice[0])
        bottom = len(self.matrice)

        if self.cox == 0:
            left = 1

        if self.coy == 0:
            top = 1

        if self.coy == bottom:
            bottom_OOR += 1

        if self.cox == right:
            right_OOR += 1

        if self.matrice[self.coy][self.cox] == 0:

            for i in range(top - 1, 2 - bottom_OOR, 1):
                for j in range(left - 1, 2 - right_OOR, 1):

                    if self.matrice[self.coy + i][self.cox + j] == 1:
                        cmpt += 1
                        print("oui !")
            if cmpt == 3:
                self.temp_matrice[self.coy][self.cox] = 1  # Modifier la copie temporaire
                return self.temp_matrice

            else:
                return self.matrice

        elif self.matrice[self.coy][self.cox] == 1:
            return self.matrice

    def appliquer_modifications(self):
        for row in self.temp_matrice:
            self.matrice.append(row[:])
        return self.matrice

class Cellule_vivante:
    def __init__(self, matrice, coy, cox):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
        # on créé une matrice temporaire pour pouvoir faire tous les déplacements sans risquer un effet domino
        self.temp_matrice = []
        for row in matrice:
            self.temp_matrice.append(row[:])

    def survie(self):
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
        if self.matrice[self.coy][self.cox] == 1:
            cmpt = 0
            for i in range(top - 1, 2 - bottom_or):
                for j in range(left - 1, 2 - right_or):
                    if self.matrice[self.coy + i][self.cox + j] == 1:
                        cmpt += 1
            # si la cellule a 3 ou 4 voisines avec elle compris
            if cmpt == 3 or cmpt == 4:
                return self.matrice
            else:
                self.temp_matrice[self.coy][self.cox] = 0  # Modifier la copie temporaire
                return self.temp_matrice
        else:
            print(self.cox, " = cox et coy = ", self.coy, self.matrice[self.coy][self.cox], "matrice")
            return 1

    def appliquer_modifications(self):
        for row in self.temp_matrice:
            self.matrice.append(row[:])
        return self.matrice



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


#fenêtre 2 : choix des pixels colorés
fenetre2 = Tk()



# grid
fenetre2.geometry("800x700")
x = 0
i = 0
j = 0

#tab = [[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1],[0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1]]
tab1 = Tableau(10, 10)
tab = tab1.creation_tableau()
print(tab1.creation_tableau())

def changer_couleur(bouton, x, y):
    couleur_actuelle = bouton["bg"]
    nouvelle_couleur = "white" if couleur_actuelle =="black" else "black"
    bouton.config(bg=nouvelle_couleur)
    if nouvelle_couleur == "white" :
        tab[x][y] = 0
    else :
        tab[x][y] = 1

def bouton_carre_noir(x, y):
    bouton = Button(fenetre2, height=3, width=6, bg="black", command=lambda ligne=x, colonne = y: changer_couleur(bouton, x, y))
    bouton.grid(column=x, row=y)

def bouton_carre_blanc(x, y):
    bouton = Button(fenetre2, height=3, width=6, bg="white", command=lambda ligne=x, colonne = y: changer_couleur(bouton, x, y))
    bouton.grid(column=x, row=y)


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


#fenêtre 3 : interface graphique du jeu de la vie.
fenetre3 = Tk()



# grid
fenetre3.geometry("800x700")
x = 0
i = 0
j = 0



def carre_noir(x, y):
    can1 = Canvas(fenetre3, height=50, width=50, bg="black")
    can1.grid(column=x, row=y)


def carre_blanc(x, y):
    can1 = Canvas(fenetre3, height=50, width=50, bg="white")
    can1.grid(column=x, row=y)


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

#remplacer la couleur d'une case : (penser à changer la grille aussi !!)
'''can1 = Canvas(fen1, height=40, width=40, bg="white")
can1.grid(column=1, row=1)'''



# bouton de sortie

bouton=Button(fenetre3, text="Fermer", command=fenetre3.quit)
bouton.grid(column=3, row=11)

bouton=Button(fenetre3, text="Retour", command=fenetre3.quit)
bouton.grid(column=2, row=10)

bouton=Button(fenetre3, text="Avance", command=fenetre3.quit)
bouton.grid(column=4, row=10)

fenetre3.mainloop()