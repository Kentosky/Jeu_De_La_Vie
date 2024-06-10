# -*- coding: utf-8 -*-
# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

""" ~~~ PARTIE DÉCLARATIVE ~~~ """
# --- La bibliothèque permettant de faire les graphismes --- #
from tkinter import *
import sys
import pygame
import Structures
import Cellule as Cell
import Tableau as Tab

largeur_ecran = 800
hauteur_ecran_sans_boutons = 460
hauteur_ecran = hauteur_ecran_sans_boutons + 40

taille_cellule = 5

if largeur_ecran // taille_cellule != 0 :
    largeur_ecran += largeur_ecran%taille_cellule
if hauteur_ecran_sans_boutons // taille_cellule != 0 :
    hauteur_ecran_sans_boutons += hauteur_ecran_sans_boutons%taille_cellule
x_matrice = int(largeur_ecran/taille_cellule)
y_matrice = int(largeur_ecran/taille_cellule)

blanc = (255, 255, 255)
noir = (0, 0, 0)
couleur_bordure = (224, 224, 224)

sensibilite_zomm = 0.1
izoom = 1
zoom_max = 5.0
zoom_min = 0.1

couleur_curseur = (150, 150, 150)
curseur_largeur = 10
curseur_longueur = 50

""" ~~~ PARTIE FONCTIONNELLE ~~~ """
""" ~~~ MISE EN PLACE DES BONUS : configurations prédéfinies de matrices afin d'obtenir un résultat en particulier dans le jeu~~~ """

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
tab1=Tab.Tableau(x_matrice, y_matrice)
matrice = tab1.creation_tableau()
#-------


def dessiner_grille_1(ecran, matrice, facteur_zoom, decalage_x, decalage_y):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else noir
            rect_cellule = pygame.Rect(x * taille_cellule * facteur_zoom + decalage_x,
                                        y * taille_cellule * facteur_zoom + decalage_y,
                                        taille_cellule * facteur_zoom,
                                        taille_cellule * facteur_zoom)
            pygame.draw.rect(ecran, couleur, rect_cellule)
            pygame.draw.rect(ecran, couleur_bordure, rect_cellule, 1)

# Fonction pour inverser la couleur d'une cellule de la grille
def inverser_couleur_pixel(x, y):
    if 0 <= y < len(matrice) and 0 <= x < len(matrice[0]):
        matrice[y][x] = 1 - matrice[y][x]

pygame.init()
ecran = pygame.display.set_mode((largeur_ecran+200, hauteur_ecran))

#_________________________définition des variables_________________________
facteur_zoom = 5
decalage_x = 0
decalage_y = 0

curseur_x = largeur_ecran // 2
curseur_y = hauteur_ecran // 2
deplacement_curseur_x = 0
deplacement_curseur_y = 0

#variables des boutons-----------------------------------------------------
#définition des couleurs :
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

#définition des polices d'écriture et des textes :
smallfont = pygame.font.SysFont('Corbel',20)
confirmer = smallfont.render('confirmer' , True , color)
quitter = smallfont.render('quitter' , True , color)
suivant = smallfont.render('suivant' , True , color)
precedent = smallfont.render('précédent' , True , color)
#fin variables des boutons--------------------------------------------------



Mise_en_place_jeu = True

while Mise_en_place_jeu:
    '''
    Cette boucle va servir à la mise en place du jeu : on génère une matrice vide, donc une grille blanche.
    Ensuite, l'utilisateur survole et clique sur les cases pour les faire changer de couleur. La matrice se met à jour en même temps.
    Une fois le bouton "confirmer" cliqué : la boucle s'arrête et la fenêtre se ferme.
    On passe à la fenêtre suivante.
    '''
    pygame.draw.rect(ecran, (170, 170, 170), [largeur_ecran, 0, 200, hauteur_ecran])



    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            jeu_en_cours = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                facteur_zoom += izoom
            elif event.key == pygame.K_m:
                facteur_zoom = max(zoom_min, facteur_zoom - izoom)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  # mise à jour de la position de la souris
            x = (x - decalage_x) // (taille_cellule * facteur_zoom)
            y = (y - decalage_y) // (taille_cellule * facteur_zoom)
            inverser_couleur_pixel(x, y)  # utilisation de la fonction inverser_couleur_pixel
            print(matrice)                                                        #test de la mise à jour de la matrice

        if event.type == pygame.MOUSEBUTTONDOWN:                                                           # Si on clique la souris sur le bouton confirmer cela ferme la fenêtre
            if largeur_ecran / 2 - largeur_ecran / 6 <= mouse[0] <= largeur_ecran / 2 + largeur_ecran / 6 and hauteur_ecran -40 <= mouse[1] <= hauteur_ecran :
                Mise_en_place_jeu = False
                break


        elif event.type == pygame.KEYDOWN:                                            #si on appuie sur une touche :

            if event.key == pygame.K_UP:                                              #si la flèche vers le haut est cliquée :
                deplacement_curseur_y = -curseur_largeur // 2                         #déplacement dans l'image selon les -y

            elif event.key == pygame.K_DOWN:                                          #si la flèche vers le bas est cliquée :
                deplacement_curseur_y = curseur_largeur // 2                          #déplacement dans l'image selon les y

            elif event.key == pygame.K_LEFT:                                          #si la flèche vers la gauche est cliquée :
                deplacement_curseur_x = -curseur_longueur // 2                        #déplacement dans l'image selon les -x

            elif event.key == pygame.K_RIGHT:                                         #si la flèche vers la droite est cliquée :
                deplacement_curseur_x = curseur_longueur // 2                         #déplacement dans l'image selon les x

        elif event.type == pygame.KEYUP:                                              #si on relâche sur une touche :
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                deplacement_curseur_y = 0                                             #on arrête tout déplacement en x et y
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                deplacement_curseur_x = 0


    # mise en place des boutons--------------------------------------------------
    # La couleur du bouton change si il est survolé par la souris
    if largeur_ecran / 2 - largeur_ecran / 6 <= mouse[0] <= largeur_ecran / 2 + largeur_ecran / 6 and hauteur_ecran - 40 <= mouse[1] <= hauteur_ecran:
        pygame.draw.rect(ecran, color_light,
                         [largeur_ecran / 2 - largeur_ecran / 6, hauteur_ecran - 40, largeur_ecran / 3, 40])
    else:
        pygame.draw.rect(ecran, color_dark,
                         [largeur_ecran / 2 - largeur_ecran / 6, hauteur_ecran - 40, largeur_ecran / 3, 40])


    #mise en place du texte des boutons-------------------------------------------
    ecran.blit(confirmer, (largeur_ecran / 2 - largeur_ecran / 17, hauteur_ecran - 30))

    #rafraichissement de la page
    pygame.display.update()

    # curseurs de déplacement-----------------------------------------------------
    curseur_x = min(max(curseur_x + deplacement_curseur_x, 0), largeur_ecran - curseur_longueur) #mise à jour les positions des curseurs
    curseur_y = min(max(curseur_y + deplacement_curseur_y, 0), hauteur_ecran - curseur_largeur)

    decalage_x = curseur_x - largeur_ecran // 2                                       #calcul du déplacement de l'image en fonction de la position des curseurs
    decalage_y = curseur_y - hauteur_ecran // 2

    ecran.fill(blanc)
    dessiner_grille_1(ecran, matrice, facteur_zoom, decalage_x, decalage_y)

    pygame.draw.rect(ecran, couleur_curseur, (curseur_x, hauteur_ecran - curseur_largeur, curseur_longueur, curseur_largeur)) #Dessin des curseurs de déplacement
    pygame.draw.rect(ecran, couleur_curseur, (largeur_ecran - curseur_largeur, curseur_y, curseur_largeur, curseur_longueur))
    # fin curseurs de déplacement-----------------------------------------------------

pygame.quit()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
taille_cellule = 5

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de la Vie")
clock = pygame.time.Clock()

# Création d'une surface pour la carte
MAP_WIDTH, MAP_HEIGHT = 1600, 1200
map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))

# Mise à jour de l'état du jeu
matrice_temp = [row[:] for row in matrice]


# Position initiale de la caméra centrée
camera_x = (MAP_WIDTH - largeur) // 2
camera_y = (MAP_HEIGHT - hauteur) // 2
camera_speed = 5
new_ecran = pygame.transform.scale(map_surface, (800, 600))

running = True
while running:
    ecran.fill(blanc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                facteur_zoom += izoom
            elif event.key == pygame.K_m:
                facteur_zoom -=  izoom

    # Gestion des touches pour déplacer la caméra
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x = max(camera_x - camera_speed, 0)
    if keys[pygame.K_RIGHT]:
        camera_x = min(camera_x + camera_speed, MAP_WIDTH - largeur)
    if keys[pygame.K_UP]:
        camera_y = max(camera_y - camera_speed, 0)
    if keys[pygame.K_DOWN]:
        camera_y = min(camera_y + camera_speed, MAP_HEIGHT - hauteur)

    # Dessin de la partie visible de la carte sur la fenêtre
    ecran.blit(map_surface, (0, 0), (camera_x, camera_y, largeur, hauteur))
    pygame.display.flip()


    for y in range(len(matrice)-1):
        for x in range(len(matrice[y])-1):
            ma_cell = Cell.Cellule(matrice, y, x, matrice_temp)
            ma_cell.regle()
#applications de la fonctions règle qui modifie l'état des cellules
for y in range(len(matrice)-1):
    for x in range(len(matrice[y])-1):
        ma_cell = Cell.Cellule(matrice, y, x, matrice_temp)
        ma_cell.regle()

#copie de la matrice
matrice = [row[:] for row in matrice_temp]
print("\nmatrice apres modifications :")
for row in matrice:
    print(row)




    matrice = [row[:] for row in matrice_temp]

    # Dessin de la grille
    dessiner_grille_1(map_surface, matrice, facteur_zoom, decalage_x, decalage_y)
    pygame.time.delay(1)
    pygame.display.flip()
    clock.tick(10)  # Limite le jeu à 10 images par seconde

pygame.quit()
sys.exit()