import pygame
import sys

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

def deuxLapins(matrice, cox, coy):
    for i in range(2):
        matrice[coy - i - 2][cox + 1] = 1
        matrice[coy - i - 1][cox + 5] = 1
        for j in range(2, 4, 2):
            matrice[coy + i][cox + j] = 1
            matrice[coy + i][cox + j + 4] = 1
    matrice[coy + 3][cox+ 7] = 1


# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
taille_cellule = 20

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur-10 , hauteur-10 ))
pygame.display.set_caption("Jeu de la Vie")

# Création du tableau et ajout de cellules vivantes
##### RAJOUTER LIGNE 263 #####
mon_tab = Tableau(largeur // taille_cellule, hauteur // taille_cellule)
matrice = mon_tab.tableau_de_tableaux
matrice[3][3] = 1
matrice[3][4] = 1
matrice[3][5] = 1
matrice[3][6] = 1
matrice[3][7] = 1


penntadeca(matrice, 10,10)
penntadeca(matrice, 13,11)
'''
matrice[154][152] = 1
matrice[153][153] = 1
matrice[152][153] = 1
matrice[152][151] = 1
matrice[152][152] = 1
'''
clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    ecran.fill(blanc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de l'état du jeu
    matrice_temp = [row[:] for row in matrice]
    for y in range(len(matrice)-1):
        for x in range(len(matrice[y])-1):
            ma_cell = Cellule(matrice, y, x, matrice_temp)
            ma_cell.regle()
    matrice = [row[:] for row in matrice_temp]

    # Dessin de la grille
    dessiner_grille(ecran, matrice, taille_cellule)
    pygame.time.delay(1)
    pygame.display.flip()
    clock.tick(10)  # Limite le jeu à 10 images par seconde

pygame.quit()
sys.exit()
