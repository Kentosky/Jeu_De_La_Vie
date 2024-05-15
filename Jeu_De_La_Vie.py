# -*- coding: utf-8 -*-
# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

""" ~~~ PARTIE DÉCLARATIVE ~~~ """

from tkinter import *
import pygame

largeur_ecran = 800
hauteur_ecran = 600

taille_cellule = 10

blanc = (255, 255, 255)
noir = (0, 0, 0)

sensibilite_zomm = 0.1
izoom = 0.1
zoom_max = 5.0
zoom_min = 0.1

couleur_curseur = (150, 150, 150)
curseur_largeur = 10
curseur_longueur = 50

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

def cligno(matrice, cox, coy):
    for i in range(3):
        matrice[coy+i][cox] = 1
    return matrice

def hamecon(matrice, cox, coy):
    for i in range(3):
        matrice[coy+i][cox] = 1
    matrice[coy][cox-1] = 1
    matrice[coy+3][cox+1] = 1
    matrice[coy+3][cox+2] = 1
    matrice[coy+2][cox+2] = 1
    return matrice
def hamecon2(matrice, cox, coy):
    for i in range(5):
        matrice[coy-i-1][cox+i] = 1
    for i in range(6):
        matrice[coy-i][cox+i] = 1
    matrice[coy-1][cox+1] = 0
    matrice[coy-4][cox+4] = 0
    matrice[coy-3][cox+2] = 0
    matrice[coy][cox+1] = 1
    matrice[coy-2][cox+3] = 1
    matrice[coy-4][cox+5] = 1
    return matrice


def canoe(matrice, cox, coy):
    for i in range(4):
        matrice[coy+i+1][cox+i] = 1
    matrice[coy][cox] = 1
    matrice[coy][cox+1] = 1
    matrice[coy+4][cox+4] = 1
    matrice[coy+3][cox+4] = 1

def penntadeca(matrice, cox, coy):
    for i in range(10):
        matrice[coy][cox + i] = 1
    matrice[coy][cox + 2] = 0
    matrice[coy][cox + 7] = 0
    matrice[coy + 1][cox + 2] = 1
    matrice[coy - 1][cox + 2] = 1
    matrice[coy + 1][cox + 7] = 1
    matrice[coy - 1][cox + 7] = 1
    return matrice

def croix(matrice, cox, coy):
    for i in range(4):
        matrice[coy][cox+i+2] = 1
        matrice[coy+7][cox+i+2] = 1
        matrice[coy+2+i][cox] = 1
        matrice[coy+i+2][cox+7] = 1
    for j in range(6):
        matrice[coy + 2][cox + 1 + j] = 1
        matrice[coy + 5][cox + 1 + j] = 1
    for k in range(2):
        matrice[coy + 2][cox + 3 + k] = 0
        matrice[coy + 5][cox + 3 + k] = 0
    for l in range(0, 5, 3):
        matrice[coy + 1][cox + 2 + l] = 1
        matrice[coy + 6][cox + 2 + l] = 1


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

#utiles pour test ----
tab1=Tableau(100, 100)
matrice = tab1.creation_tableau()
#-------

def dessiner_grille(ecran, matrice, facteur_zoom, decalage_x, decalage_y):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else noir
            rect_cellule = pygame.Rect(x * taille_cellule * facteur_zoom + decalage_x,
                                        y * taille_cellule * facteur_zoom + decalage_y,
                                        taille_cellule * facteur_zoom,
                                        taille_cellule * facteur_zoom)
            pygame.draw.rect(ecran, couleur, rect_cellule)

# Fonction pour inverser la couleur d'une cellule de la grille
def inverser_couleur_pixel(x, y):
    if 0 <= y < len(matrice) and 0 <= x < len(matrice[0]):
        matrice[y][x] = 1 - matrice[y][x]

pygame.init()
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))


facteur_zoom = 1
decalage_x = 0
decalage_y = 0

curseur_x = largeur_ecran // 2
curseur_y = hauteur_ecran // 2
deplacement_curseur_x = 0
deplacement_curseur_y = 0

jeu_en_cours = True

while jeu_en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:                                                            # Molette vers le haut
                facteur_zoom += izoom
            elif event.button == 5:                                                          # Molette vers le bas
                facteur_zoom = max(zoom_min, facteur_zoom - izoom)
            else:
                x, y = event.pos                                                             #mise à jour de la position de la souris
                x = (x - decalage_x) // (taille_cellule * facteur_zoom)
                y = (y - decalage_y) // (taille_cellule * facteur_zoom)
                inverser_couleur_pixel(x, y)                                                 #utilisation de la fonction inverser_couleur_pixel
                print(matrice)                                                               #test de la mise à jour de la matrice
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:                                                     #si la flèche vers le haut est cliquée :
                deplacement_curseur_y = -curseur_largeur // 2                                #déplacement dans l'image selon les -y
            elif event.key == pygame.K_DOWN:
                deplacement_curseur_y = curseur_largeur // 2
            elif event.key == pygame.K_LEFT:
                deplacement_curseur_x = -curseur_longueur // 2
            elif event.key == pygame.K_RIGHT:
                deplacement_curseur_x = curseur_longueur // 2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                deplacement_curseur_y = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                deplacement_curseur_x = 0

    #Mettre à jour les positions des curseurs
    curseur_x = min(max(curseur_x + deplacement_curseur_x, 0), largeur_ecran - curseur_longueur)
    curseur_y = min(max(curseur_y + deplacement_curseur_y, 0), hauteur_ecran - curseur_largeur)
    #Calculer le déplacement de l'image en fonction de la position des curseurs
    decalage_x = curseur_x - largeur_ecran // 2
    decalage_y = curseur_y - hauteur_ecran // 2

    ecran.fill(blanc)
    dessiner_grille(ecran, matrice, facteur_zoom, decalage_x, decalage_y)

    #Dessiner les curseurs de déplacement
    pygame.draw.rect(ecran, couleur_curseur, (curseur_x, hauteur_ecran - curseur_largeur, curseur_longueur, curseur_largeur))
    pygame.draw.rect(ecran, couleur_curseur, (largeur_ecran - curseur_largeur, curseur_y, curseur_largeur, curseur_longueur))

    pygame.display.flip()

pygame.quit()