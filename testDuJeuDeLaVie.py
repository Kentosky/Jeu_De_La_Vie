import pygame
import sys
import moviepy.editor

# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

class Tableau:
    """ Classe qui permet de créer une liste de listes qui sera ensuite interprétée comme toutes les cases du jeu de la vie. """
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.tableau_de_tableaux = self.creation_tableau()

    def creation_tableau(self):
        tableau_de_tableaux = []
        for i in range(self.largeur):
            ligne = []
            for j in range(self.longueur):
                ligne.append(0)
            tableau_de_tableaux.append(ligne)
        return tableau_de_tableaux

class Cellule:
    def __init__(self, matrice, coy, cox, temp_matrice):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
        self.temp_matrice = temp_matrice

    def regle(self):
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

        if self.matrice[self.coy][self.cox] == 1:
            cmptS = 0
            for i in range(top - 1, 2 - bottom_or):
                for j in range(left - 1, 2 - right_or):
                    if self.matrice[self.coy + i][self.cox + j] == 1:
                        cmptS += 1

            if cmptS == 3 or cmptS == 4:
                self.temp_matrice[self.coy][self.cox] = 1
            else:
                self.temp_matrice[self.coy][self.cox] = 0

        else:
            cmptN = 0
            for i in range(top - 1, 2 - bottom_or, 1):
                for j in range(left - 1, 2 - right_or, 1):
                    if self.matrice[self.coy + i][self.cox + j] == 1:
                        cmptN += 1
            if cmptN == 3:
                self.temp_matrice[self.coy][self.cox] = 1
            else:
                self.temp_matrice[self.coy][self.cox] = 0

        return self.temp_matrice

def dessiner_grille(ecran, matrice, taille_cellule):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else noir
            rect_cellule = pygame.Rect(x * taille_cellule, y * taille_cellule, taille_cellule, taille_cellule)
            pygame.draw.rect(ecran, couleur, rect_cellule)



# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

class Tableau:
    """ Classe qui permet de créer une liste de listes qui sera ensuite interprétée comme toutes les cases du jeu de la vie. """
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.tableau_de_tableaux = self.creation_tableau()

    def creation_tableau(self):
        tableau_de_tableaux = []
        for i in range(self.largeur):
            ligne = []
            for j in range(self.longueur):
                ligne.append(0)
            tableau_de_tableaux.append(ligne)
        return tableau_de_tableaux

class Cellule:
    def __init__(self, matrice, coy, cox, temp_matrice):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
        self.temp_matrice = temp_matrice

    def regle(self):
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

        if self.matrice[self.coy][self.cox] == 1:
            cmptS = 0
            for i in range(top - 1, 2 - bottom_or):
                for j in range(left - 1, 2 - right_or):
                    if self.matrice[self.coy + i][self.cox + j] == 1:
                        cmptS += 1

            if cmptS == 3 or cmptS == 4:
                self.temp_matrice[self.coy][self.cox] = 1
            else:
                self.temp_matrice[self.coy][self.cox] = 0

        else:
            cmptN = 0
            for i in range(top - 1, 2 - bottom_or, 1):
                for j in range(left - 1, 2 - right_or, 1):
                    if self.matrice[self.coy + i][self.cox + j] == 1:
                        cmptN += 1
            if cmptN == 3:
                self.temp_matrice[self.coy][self.cox] = 1
            else:
                self.temp_matrice[self.coy][self.cox] = 0

        return self.temp_matrice

def dessiner_grille(ecran, matrice, taille_cellule):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else noir
            rect_cellule = pygame.Rect(x * taille_cellule, y * taille_cellule, taille_cellule, taille_cellule)
            pygame.draw.rect(ecran, couleur, rect_cellule)

def deuxLapins(matrice, cox, coy):
    matrice[coy + 1][cox] = 1
    matrice[coy + 1][cox + 2] = 1
    matrice[coy][cox + 4] = 1
    matrice[coy][cox + 6] = 1
    matrice[coy + 1][cox + 5] = 1
    matrice[coy + 2][cox + 5] = 1
    matrice[coy + 2][cox + 1] = 1
    matrice[coy + 3][cox + 1] = 1
    matrice[coy + 3][cox + 7] = 1


# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
taille_cellule = 15

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))

ecran2 = pygame.display.set_mode((largeur, hauteur))

pygame.display.set_caption("Jeu de la Vie")

# Création du tableau et ajout de cellules vivantes
mon_tab = Tableau(largeur // taille_cellule, hauteur // taille_cellule)
matrice = mon_tab.tableau_de_tableaux

from moviepy.editor import *

pygame.init()
video = moviepy.editor.VideoFileClip("video.mp4")
video.preview()
pygame.quit()

matrice[2][2] = 1
matrice[3][2] = 1
matrice[3][3] = 1
matrice[2][3] = 1
deuxLapins(matrice, 8, 6)

clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    ecran.fill(blanc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin de la grille
    dessiner_grille(ecran, matrice, taille_cellule)
    pygame.time.delay(2000)
    pygame.display.flip()
    clock.tick(10)  # Limite le jeu à 10 images par seconde

pygame.quit()
sys.exit()