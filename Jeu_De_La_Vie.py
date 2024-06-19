# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

import sys
import pygame

import Structures
import Cellule as Cell
import Tableau as Tab
import time
from moviepy.editor import VideoFileClip
import pygame_widgets
from pygame_widgets.button import Button
# Initialisation de Pygame
pygame.init()

# Définir la taille de l'écran selon la taille de la vidéo
largeur_ecran, hauteur_ecran = 1100, 800
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
# In resize.py line 37 : change "ANTIALIAS" by "LANCZOS"
video = VideoFileClip("video.mp4").resize((1600,800))
pygame.display.set_caption("Video du menu")
couleur_rect = (255, 255, 255, 180)  # Blanc avec 50% de transparence
rect_surface = pygame.Surface((largeur_ecran,hauteur_ecran), pygame.SRCALPHA)
rect_surface.fill(couleur_rect)

# Création de notre tableau a partir de la classe Tableau
taille_cellule = 5
x_matrice = int(largeur_ecran/taille_cellule)
y_matrice = int(largeur_ecran/taille_cellule)
tableau=Tab.Tableau(x_matrice, y_matrice)
matrice = tableau.creation_tableau()

#définition des couleurs que nous utiliserons :
blanc = (255, 255, 255)
couleur_bordure = (224, 224, 224)
colors = [
    (0, 0, 0),         # Noir
    (255, 0, 0),       # Rouge
    (255, 192, 203),   # Rose
    (0, 255, 255),     # Bleu clair
    (255, 165, 0),     # Orange
    (0, 128, 0)        # Vert
]
couleur_choisie=colors[0]

#variable de zoom
facteur_zoom = 5

# Création d'une surface pour la carte
largeur_map, hauteur_map = 3200, 2400
surface_map = pygame.Surface((largeur_map, hauteur_map))

# Position initiale de la caméra centrée
camera_x = (largeur_map - largeur_ecran) // 2
camera_y = (hauteur_map - hauteur_ecran) // 2
vitesse_camera = 20 # vitesse de déplacement de la camera

# Définition la police
font = pygame.font.Font('Tiny5-regular.ttf', size = 25)
font_titre = pygame.font.Font('Tiny5-regular.ttf', size = 70)

"""
Cette fonction permet de récupérer la couleur que le joueur a choisi pour les cellules vivantes
"""
def choix_couleur(couleur):
    global couleur_choisie
    couleur_choisie = couleur
    couleur_texte = colors[0]
    cdc_couleur = "Noir"
    if couleur == colors[0]:
        cdc_couleur = "Noir"
        couleur_texte = (255, 255, 255)
    if couleur == colors[1]:
        cdc_couleur = "Rouge"
    if couleur == colors[2]:
        cdc_couleur = "Rose"
    if couleur == colors[3]:
        cdc_couleur = "Bleu Clair"
    if couleur == colors[4]:
        cdc_couleur = "Orange"
    if couleur == colors[5]:
        cdc_couleur = "Vert"
    surface_texte_couleur = font.render("Couleur choisie : " + cdc_couleur, True, couleur_texte, couleur)
    rect_texte = surface_texte_couleur.get_rect()
    rect_texte.center = (largeur_ecran // 2, 200)
    ecran.blit(surface_texte_couleur, rect_texte)
    pygame.display.update()
    time.sleep(1)
    return couleur

"""
Cette fonction permet de dessiner une grille pygame à partir de la matrice que l'on a créé précedemment
De base, chaque case de la grille est un carré blanc qui est cliquable et qui changera de couleur par la suite
"""
def dessiner_grille(ecran, matrice, facteur_zoom, couleur_choisie):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else couleur_choisie
            rect_cellule = pygame.Rect(x * taille_cellule * facteur_zoom,
                                        y * taille_cellule * facteur_zoom,
                                        taille_cellule * facteur_zoom,
                                        taille_cellule * facteur_zoom)
            pygame.draw.rect(ecran, couleur, rect_cellule) # dessin des cases
            pygame.draw.rect(ecran, couleur_bordure, rect_cellule, 1) # dessin des bordures de cases

"""
Cette fonction permet d'inverser la couleur d'un pixel afin de faire naitre 
et faire mourir des cellules
"""
def inverser_couleur_pixel(x, y):
    if 0 <= y < len(matrice) and 0 <= x < len(matrice[0]):
        matrice[y][x] = 1 - matrice[y][x]

"""
Cette fonction permet de zoomer et dezoomer le tableau 
lorsque l'on est dans la partie édition ou dans le jeu
"""
def zoom(event, facteur_zoom):
    if event.type == pygame.KEYDOWN:
        # zoom
        if event.key == pygame.K_p:
            facteur_zoom = min(10, facteur_zoom + 1)
        # dezoom
        elif event.key == pygame.K_m:
            facteur_zoom = max(1, facteur_zoom - 1)
    return facteur_zoom

"""
Cette fonction permet de se déplacer dans le tableau 
lorsque l'on est dans la partie édition ou dans le jeu
"""
def deplacement(camera_x, camera_y, vitesse_camera, largeur_ecran, hauteur_ecran, largeur_map, hauteur_map):
    keys = pygame.key.get_pressed()
    # deplacement selon la flèche gauche
    if keys[pygame.K_LEFT]:
        camera_x = max(camera_x - vitesse_camera, 0)
    # deplacement selon la flèche droite
    if keys[pygame.K_RIGHT]:
        camera_x = min(camera_x + vitesse_camera, largeur_map - largeur_ecran)
    # deplacement selon la flèche haute
    if keys[pygame.K_UP]:
        camera_y = max(camera_y - vitesse_camera, 0)
    # deplacement selon la flèche basse
    if keys[pygame.K_DOWN]:
        camera_y = min(camera_y + vitesse_camera, hauteur_map - hauteur_ecran)
    return camera_x, camera_y

"""
Cette fonction est la fonction de menu:
Celle-ci affiche 3 boutons (Jouer, Règles et Quitter)
"""
def show_menu():
    global state, jouer, quitter, regle, parametre
    state = "menu"
    # telechargement et redimmension de l'image parametre
    img_parametre = pygame.image.load("parametre.png")
    parametre_redim = pygame.transform.scale(img_parametre, (20,20))
    # Création du bouton Jouer
    jouer = Button(
        ecran,  # ecran choisi
        largeur_ecran // 2 - 150,   # coordonnes x bouton
        hauteur_ecran // 2 - 250,  # coordonnes y bouton
        300,  # largeur
        100,  # hauteur

        # Paramètres bouton
        text='JOUER',  # Text
        fontSize=69,  # taille police
        margin=20,  # centrer le texte
        inactiveColour=(0, 100, 60),  # couleur bouton inactif
        hoverColour=(50, 150, 112),  # couleur bouton souris dessus
        pressedColour=(0, 200, 20),  # couleur bouton cliqué
        radius=20,  # arrondissement des angles du bouton
        onClick=edition  # appel fonction edition
    )

    # Création du bouton Quitter
    quitter = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran // 2 - 150,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran // 2 + 150,  # Coordonnée y du coin supérieur gauche
        300,  # Largeur
        100,  # Hauteur

        # Paramètres du bouton
        text='QUITTER',  # Texte à afficher
        fontSize=69,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=lambda: quit()  # Fonction à appeler lors du clic
    )

    # Création du bouton Règles
    regle = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran // 2 - 150,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran // 2 - 50,  # Coordonnée y du coin supérieur gauche
        300,  # Largeur
        100,  # Hauteur

        # Paramètres du bouton
        text='RÈGLES',  # Texte à afficher
        fontSize=69,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=show_rules  # Fonction à appeler lors du clic
    )
    #Creation du bouton parametre
    parametre = Button(
        ecran,  # Surface sur laquelle placer le bouton
        10,  # Coordonnée x du coin supérieur gauche
        10,  # Coordonnée y du coin supérieur gauche
        20,  # Largeur
        20,  # Hauteur

        # Paramètres du bouton
        image=parametre_redim,
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=show_parametre  # Fonction à appeler lors du clic
    )
def show_parametre():
    global state, retour_menu,btn_rouge,btn_noir,btn_rose,btn_vert,btn_bleu,btn_orange
    state = "parametre"

    # Création du bouton Retour au Menu
    retour_menu = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 170,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran - 70,  # Coordonnée y du coin supérieur gauche
        150,  # Largeur
        50,  # Hauteur

        # Paramètres optionnels
        text='MENU',  # Texte à afficher
        fontSize=30,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=show_menu  # Fonction à appeler lors du clic
    )
    # Creation des differents boutons
    btn_noir = Button(
        ecran,  # Surface sur laquelle placer le bouton
        460,  # Coordonnée x du coin supérieur gauche
        270,  # Coordonnée y du coin supérieur gauche
        30,  # Largeur
        30,  # Hauteur
        inactiveColour=colors[0],  # Couleur du bouton inactif
        # appel de la fonction choix_couleur
        onClick=lambda: choix_couleur(colors[0])
    )
    btn_rouge = Button(
        ecran,  # Surface sur laquelle placer le bouton
        490,  # Coordonnée x du coin supérieur gauche
        270,  # Coordonnée y du coin supérieur gauche
        30,  # Largeur
        30,  # Hauteur
        inactiveColour=colors[1],  # Couleur du bouton inactif
        onClick=lambda: choix_couleur(colors[1])  # Fonction à appeler lors du clic
    )
    btn_rose = Button(
        ecran,  # Surface sur laquelle placer le bouton
        520,  # Coordonnée x du coin supérieur gauche
        270,  # Coordonnée y du coin supérieur gauche
        30,  # Largeur
        30,  # Hauteur
        inactiveColour=colors[2],  # Couleur du bouton inactif
        onClick=lambda: choix_couleur(colors[2])  # Fonction à appeler lors du clic
    )
    btn_bleu = Button(
        ecran,  # Surface sur laquelle placer le bouton
        550,  # Coordonnée x du coin supérieur gauche
        270,  # Coordonnée y du coin supérieur gauche
        30,  # Largeur
        30,  # Hauteur
        inactiveColour=colors[3],  # Couleur du bouton inactif
        onClick=lambda: choix_couleur(colors[3])  # Fonction à appeler lors du clic
    )
    btn_orange = Button(
        ecran,  # Surface sur laquelle placer le bouton
        580,  # Coordonnée x du coin supérieur gauche
        270,  # Coordonnée y du coin supérieur gauche
        30,  # Largeur
        30,  # Hauteur
        inactiveColour=colors[4],  # Couleur du bouton inactif
        onClick=lambda: choix_couleur(colors[4])  # Fonction à appeler lors du clic
    )
    btn_vert = Button(
        ecran,  # Surface sur laquelle placer le bouton
        610,  # Coordonnée x du coin supérieur gauche
        270,  # Coordonnée y du coin supérieur gauche
        30,  # Largeur
        30,  # Hauteur
        inactiveColour=colors[5],  # Couleur du bouton inactif
        onClick=lambda: choix_couleur(colors[5])  # Fonction à appeler lors du clic
    )




"""
Cette fonction est la fonction de règles:
Celle-ci affiche les règles du jeu pour le joueur 
"""
def show_rules():
    global state, retour_menu
    state = "rules"
    # Création du bouton Retour au Menu
    retour_menu = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 170,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran - 70,  # Coordonnée y du coin supérieur gauche
        150,  # Largeur
        50,  # Hauteur

        # Paramètres optionnels
        text='MENU',  # Texte à afficher
        fontSize=30,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=show_menu  # Fonction à appeler lors du clic
    )

def reinitialise():
    global matrice
    for i in range(len(matrice)):  # la liste de listes fera une largeur de la variable largeur
        for j in range(len(matrice[0])):  # la liste de listes fera une longueur de la variable longueur
            matrice[i][j] = 0
    return matrice

"""
Cette fonction est la fonction d'édition:
Celle-ci permet au joueur de dessiner a sa guise ou bien, a partir des formes préfaites,
de découvrir comment fonctionne les cellules entre elles dans le jeu.
Il peut se déplacer, zoomer et dézoomer afin d'avoir une surface de dessin plus grande
"""
def edition():
    global state, matrice, camera_x, camera_y, facteur_zoom, retour_menu
    state = "edition"
    pygame.init()

    # Variables pour les boutons
    # Création du bouton Retour au Menu 2
    retour_menu_2 = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 465,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran - 90,  # Coordonnée y du coin supérieur gauche
        150,  # Largeur
        50,  # Hauteur

        # Paramètres du bouton
        text='MENU',  # Texte à afficher
        fontSize=30,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=40,  # Rayon pour arrondir les coins du bouton
        onClick=show_menu  # Fonction à appeler lors du clic
    )

    # Création du bouton Commencer le Jeu
    jeuB = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 650,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran - 90,  # Coordonnée y du coin supérieur gauche
        175,  # Largeur
        50,  # Hauteur

        # Paramètres du bouton
        text='COMMENCER',  # Texte à afficher
        fontSize=30,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=jeu  # Fonction à appeler lors du clic
    )

    reini = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 860,  # Coordonnée x du coin supérieur gauche
        hauteur_ecran - 90,  # Coordonnée y du coin supérieur gauche
        200,  # Largeur
        50,  # Hauteur

        # Paramètres du bouton
        text='RÉINITIALISER',  # Texte à afficher
        fontSize=30,  # Taille de la police
        margin=20,  # Marge pour centrer le texte
        inactiveColour=(200, 50, 0),  # Couleur du bouton inactif
        hoverColour=(150, 0, 0),  # Couleur du bouton survolé
        pressedColour=(0, 200, 20),  # Couleur du bouton enfoncé
        radius=40,  # Rayon pour arrondir les coins du bouton
        onClick=reinitialise  # Fonction à appeler lors du clic
    )

    #############################Definition des boutons et initialisation des images pour le menu édition#############################
    #Importation des images au format png
    croix = pygame.image.load("croix.png")
    canoe = pygame.image.load("canoe.png")
    spacefighter = pygame.image.load("spacefighter.png")
    hamecon = pygame.image.load("hamecon.png")
    hamecon2 = pygame.image.load("hamecon2.png")
    penntadeca = pygame.image.load("pentadeca.png")
    deuxLapins = pygame.image.load("deux_lapins.png")

    # On définit la nouvelle taille de l'image afin que toutes aient la même taille :
    largeur_hauteur_image = (100, 100)

    # On redimensionne chaque image
    croix_redim = pygame.transform.scale(croix, largeur_hauteur_image)
    canoe_redim = pygame.transform.scale(canoe, largeur_hauteur_image)
    spacefighter_redim = pygame.transform.scale(spacefighter, largeur_hauteur_image)
    hamecon_redim = pygame.transform.scale(hamecon, largeur_hauteur_image)
    hamecon2_redim = pygame.transform.scale(hamecon2, largeur_hauteur_image)
    penntadeca_redim = pygame.transform.scale(penntadeca, largeur_hauteur_image)
    deuxLapins_redim = pygame.transform.scale(deuxLapins, largeur_hauteur_image)

    # Création du bouton Canoë
    canoe_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 275,  # Coordonnée x du coin supérieur gauche
        50,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=canoe_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Croix
    croix_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 125,  # Coordonnée x du coin supérieur gauche
        50,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=croix_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton spacefighter
    spacefighter_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 275,  # Coordonnée x du coin supérieur gauche
        200,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=spacefighter_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )


    # Création du bouton Hameçon
    hamecon_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 125,  # Coordonnée x du coin supérieur gauche
        200,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=hamecon_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Hameçon 2
    hamecon2_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 275,  # Coordonnée x du coin supérieur gauche
        350,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=hamecon2_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Penntadeca
    penntadeca_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 125,  # Coordonnée x du coin supérieur gauche
        350,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=penntadeca_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Deux Lapins
    deuxLapins_btn = Button(
        ecran,  # Surface sur laquelle placer le bouton
        largeur_ecran - 275,  # Coordonnée x du coin supérieur gauche
        500,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=deuxLapins_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )
    # si on est dans l'état menu on affiche les 3 boutons

    def convertir_pos_matrice(x, y):
        '''Cette fonction prend en paramètres x et y qui sont les coordonnées du curseur par rapport au canva.
        Elle renvoie x1 et y1 qui sont les coordonnées converties pour correspondre aux cellules de la matrice.
        '''
        x1 = (x + camera_x) // (taille_cellule * facteur_zoom)
        y1 = (y + camera_y) // (taille_cellule * facteur_zoom)
        return x1, y1

    def mode_actif(cdc):
        '''Cette fonction prend en paramètre une chaine de caractères cdc.
        Elle affiche un texte sur fond coloré complété par celui donné en paramètres.'''
        surface_texte = font.render("Insertion : " + cdc, True, colors[0],(125, 255, 175))
        rect_texte = surface_texte.get_rect()
        rect_texte.center = ((largeur_ecran - 300)// 2, 30)
        ecran.blit(surface_texte, rect_texte)                       # Affichage du texte

    #Mise en place des modes de dessin : drawing = False tant que le second clic n'a pas été fait.
    #Quand on clique sur le Canva après avoir cliqué sur une image de forme prédéfinie, drawing = True :
    #On peut maintenant placer la figure aux coordonnées sur lesquelles nous cliquons.
    drawing = False
    drawing_canoe=False
    drawing_croix=False
    drawing_spacefighter=False
    drawing_hamecon=False
    drawing_hamecon2=False
    drawing_penntadeca=False
    drawing_deuxLapins=False


    if state == "menu":
        jouer.draw()
        quitter.draw()
        regle.draw()
    # tant qu'on est dans l'état édition :
    while state == "edition":
        for event in pygame.event.get():
            retour_menu_2.listen(pygame.event.get())               #On met à jour régulièrement l'état du bouton retour_menu_2
            jeuB.listen(pygame.event.get())
            reini.listen(pygame.event.get())
            if event.type == pygame.QUIT:
                pygame.quit()                                       #La fenêtre se ferme et le programme s'arrête si le bouton quitter est cliqué
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                retour_menu_2.draw()                               #On place le bouton retour_menu_2
                x, y = event.pos                                    #on relève les coordonnées de la souris

                '''On met en place les conditions pour savoir quelle image afficher lorsque l'on clique sur une image
                représentant une forme prédéfinie.'''
                #Si on appuie dans la zone correspondant au bouton Canoe :
                if (largeur_ecran-275 <= x <= largeur_ecran-175) and (50 <= y <= 150) :
                    if event.button == 1 :
                        if not drawing:                             # Ce premier clic prépare le placement du rectangle
                            drawing_canoe = True
                            break                                   # On arrête la boucle pour ne pas entrer dans les autres conditions if


                # Si on appuie dans la zone correspondant au bouton Croix :
                elif (largeur_ecran-125 <= x <= largeur_ecran-25) and (50 <= y <= 150) :
                    if event.button == 1 :
                        if not drawing:
                            drawing_croix = True
                            break

                # Si on appuie dans la zone correspondant au bouton spacefighter :
                elif (largeur_ecran-275 <= x <= largeur_ecran-175) and (200 <= y <= 300) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_spacefighter = True
                            break

                # Si on appuie dans la zone correspondant au bouton Hameçon :
                elif (largeur_ecran-125 <= x <= largeur_ecran-25) and (200 <= y <= 300) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_hamecon = True
                            break

                # Si on appuie dans la zone correspondant au bouton Hameçon 2 :
                elif (largeur_ecran-275 <= x <= largeur_ecran-175) and (350 <= y <= 450) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_hamecon2 = True
                            break

                # Si on appuie dans la zone correspondant au bouton Penta décathlon:
                elif (largeur_ecran-125 <= x <= largeur_ecran-25) and (350 <= y <= 450) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_penntadeca = True
                            break

                # Si on appuie dans la zone correspondant au bouton Deux Lapins :
                elif (largeur_ecran-275 <= x <= largeur_ecran-175) and (500 <= y <= 600) :
                    if event.button == 1 :
                        if not drawing:
                            drawing_deuxLapins = True
                            break

                else :
                    '''Conditions pour tracer les images à partir du second Clic (donc après avoir sélectionné l'image)'''
                    if drawing_canoe == True :
                        x, y = convertir_pos_matrice(x, y)                  #On convertit les coordonnées de la souris en coordonnées de la matrice.
                        Structures.canoe(matrice, x, y)                     #On trace la figure avec la fonction canoe, qui provient du fichier Structures.py
                        drawing_canoe=False                                 #On réinitialise les variables drawing pour éviter de dessiner plusieurs figures à la suite
                        drawing = False
                        break                                               #On quitte la boucle pour la recommencer

                    if drawing_croix == True :                              #On réitère le même procédé avec la figure Croix
                        x, y = convertir_pos_matrice(x, y)
                        Structures.croix(matrice, x, y)
                        drawing_croix=False
                        drawing = False
                        break

                    if drawing_spacefighter == True :
                        x, y = convertir_pos_matrice(x, y)
                        Structures.spacefighter(matrice, x, y)
                        drawing_spacefighter=False
                        drawing = False
                        break

                    if drawing_hamecon == True :
                        x, y = convertir_pos_matrice(x, y)
                        Structures.hamecon(matrice, x, y)
                        drawing_hamecon=False
                        drawing = False
                        break

                    if drawing_hamecon2 == True :
                        x, y = convertir_pos_matrice(x, y)
                        Structures.hamecon2(matrice, x, y)
                        drawing_hamecon2=False
                        drawing = False
                        break

                    if drawing_penntadeca == True :
                        x, y = convertir_pos_matrice(x, y)
                        Structures.penntadeca(matrice, x, y)
                        drawing_penntadeca=False
                        drawing = False
                        break

                    if drawing_deuxLapins == True :
                        x, y = convertir_pos_matrice(x, y)
                        Structures.deuxLapins(matrice, x, y)
                        drawing_deuxLapins=False
                        drawing = False
                        break



                x, y = convertir_pos_matrice(x, y)                          #Si aucune des conditions précédentes n'est satisfaite : on convertit les coordonnées en coordonnées de la matrice
                inverser_couleur_pixel(x, y)                                # quand une case est cliquée elle change de couleur.
                pygame.display.flip()                                       #On met à jour le canva


            facteur_zoom = zoom(event, facteur_zoom)
        camera_x, camera_y = deplacement(camera_x, camera_y, vitesse_camera, largeur_ecran, hauteur_ecran, largeur_map,hauteur_map)
        ecran.fill((255, 255, 255))
        ecran.blit(surface_map, (0, 0), (camera_x, camera_y, largeur_ecran, hauteur_ecran))
        dessiner_grille(surface_map, matrice, facteur_zoom,couleur_choisie)


        #### Fonctions d'affichage du mode en cours : un texte avec fond coloré s'affiche tant qu'une image est sélectionnée ####
        if drawing_canoe:
            mode_actif("Canoe")
        if drawing_croix:
            mode_actif("Croix")
        if drawing_spacefighter:
            mode_actif("Spacefighter")
        if drawing_hamecon:
            mode_actif("Hameçon")
        if drawing_hamecon2:
            mode_actif("Hameçon 2")
        if drawing_penntadeca:
            mode_actif("Pentadecathlon")
        if drawing_deuxLapins:
            mode_actif("Deux Lapins")

        #Ce rectangle gris est le fond de la fenêtre d'affichage des images des formes prédéfinies
        pygame.draw.rect(ecran, (170, 170, 170), [largeur_ecran - 300, 0, 300, hauteur_ecran])

        #On affiche tous les boutons
        canoe_btn.draw()
        croix_btn.draw()
        spacefighter_btn.draw()
        hamecon_btn.draw()
        hamecon2_btn.draw()
        penntadeca_btn.draw()
        deuxLapins_btn.draw()

        #On affiche les boutons de déplacement entre les menus / de sortie de la fenêtre
        jeuB.draw()
        retour_menu_2.draw()
        reini.draw()
        pygame.display.flip()

    state = "menu"

"""
Cette fonction est la fonction de jeu:
Celle-ci reprend le schéma dessiner par le joueur dans la partie édition et 
effectue les regles de survie établie par le jeu
Le joueur pourra zoomer,dézoomer, se déplacer et surtout contempler les cellules se développer
"""
def jeu():
    global matrice, camera_x, camera_y, facteur_zoom
    # On gère la musique du jeu
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("son_jdv2.mp3")
    pygame.mixer.music.play(10, 0.0)
    clock = pygame.time.Clock()

    # Implémentation d'un bouton quitter :
    quitter_2 = Button(
        ecran,  # Surface to place button on
        largeur_ecran - 120,  # X-coordinate of top left corner
        hauteur_ecran - 60,  # Y-coordinate of top left corner
        100,  # Width
        40,  # Height
        # Optional Parameters
        text='QUITTER',  # Text to display
        fontSize=25,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=40,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: pygame.quit() or sys.exit()  # Function to call when clicked on
    )
    retour_menu_3= Button(
        ecran,  # Surface to place button on
        largeur_ecran - 230,  # X-coordinate of top left corner
        hauteur_ecran - 60,  # Y-coordinate of top left corner
        100,  # Width
        40,  # Height
        # Optional Parameters
        text='MENU',  # Text to display
        fontSize=25,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=40,  # Radius of border corners (leave empty for not curved)
        onClick=main  # Function to call when clicked on
    )

    # Mise à jour de l'état du jeu et création de la matrice temporaire pour la modification
    matrice_temp = [row[:] for row in matrice]
    running = True
    while running:
        ecran.fill((255, 255, 255))

        # Gestion des événements
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # Gestion du zoom avec appel de la fonction
            facteur_zoom = zoom(event, facteur_zoom)
        #bouton quitter
        quitter_2.listen(events)
        retour_menu_3.listen(events)

        # Gestion du déplacement avec appel de la fonction
        camera_x, camera_y = deplacement(camera_x, camera_y, vitesse_camera, largeur_ecran, hauteur_ecran, largeur_map,hauteur_map)
        # Dessin de la partie visible de la carte sur la fenêtre
        ecran.blit(surface_map, (0, 0), (camera_x, camera_y, largeur_ecran, hauteur_ecran))

        # Applications de la fonction règle qui modifie l'état des cellules
        for y in range(len(matrice) - 1):
            for x in range(len(matrice[y]) - 1):
                # Création de toutes les cellules présentes sur la map et application des règles
                ma_cell = Cell.Cellule(matrice, y, x, matrice_temp)
                ma_cell.regle()

        # Copie de la matrice
        matrice = [row[:] for row in matrice_temp]
        # Dessin de la grille
        dessiner_grille(surface_map, matrice, facteur_zoom,couleur_choisie)
        # Dessin du bouton quitter
        quitter_2.draw()
        retour_menu_3.draw()

        # Mise à jour de la fenetre
        pygame.display.flip()
        clock.tick(10)  # Limite le jeu à 10 images par seconde

    pygame.quit()
    sys.exit()

# Modification de la fonction main pour inclure l'état edition
def main():
    global state

    pygame.mixer.init()                             # Initialisation du mixer pour la musique in game
    pygame.mixer.music.load("son_jdv.mp3")          # Load du son trop cool
    pygame.mixer.music.play(10, 0.0)    # Lancement de la musique (elle se répetera 10 fois

    show_menu()  # Afficher le menu principal

    state = "menu"
    running = True          # On initialise le jeu à True
    video_start_time = pygame.time.get_ticks()      # Démarrage de la vidéo du menu
    while running:                                  # Boucle principale
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # Condition d'arrêt
                running = False
            pygame_widgets.update(event)            # Gestion des événements Pygame et des widgets

        # Calculer le temps écoulé depuis le début de la vidéo
        elapsed_time = (pygame.time.get_ticks() - video_start_time) / 1000

        # Obtenir l'image actuelle de la vidéo
        frame = video.get_frame(elapsed_time)

        # Convertir l'image en surface Pygame
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        # Calculer les coordonnées pour centrer la vidéo
        video_width, video_height = frame_surface.get_size()
        x = (largeur_ecran - video_width) // 2 - 80
        y = (hauteur_ecran - video_height) // 2

        # Afficher l'image
        ecran.blit(frame_surface, (x, y))
        ecran.blit(rect_surface, (0, 0))

        titre = "Le Jeu de la Vie"
        titre_police = font_titre.render(titre, True, colors[0])
        ecran.blit(titre_police, (340, 30))

        if state == "menu":         # Condition pour revenir au menu
            jouer.draw()
            quitter.draw()
            regle.draw()
            parametre.draw()
        elif state == "rules":      # Ou aller aux règles
            # Afficher le texte des règles
            rules_text = [
                "  ", " ", " ", " Le jeu de la vie : des règles simples, une infinité de résolutions.", "",
                "Le jeu de la vie c’est 2 règles : Règle de survie, règle de naissance. ", "",
                "Au début vous devrez choisir la taille du tableau puis la remplir comme vous le souhaitez, ",
                "par la suite, vous verrez le développement des cellules*.",
                "A savoir que si une cellule* ne survit pas, elle meurt.", "*cellule = case pleine", "",
                "Règle de survie : ",
                "Si une cellule est entourée de plus d’1 cellule et de moins de 4 cellules, elle survit au",
                " prochain tour.", "", "Règle de naissance :",
                "Si une case vide est entourée de exactement 3 cases, alors elle sera vivante le tour", " d’après."
            ]
            y_offset = 8
            for line in rules_text:
                text_surface = font.render(line, True, colors[0])
                ecran.blit(text_surface, (70, y_offset))
                y_offset += 40

            # Dessiner le bouton pour revenir au menu
            retour_menu.draw()
        elif state == "parametre":
            show_parametre()
            retour_menu.draw()
            btn_noir.draw()
            btn_rouge.draw()
            btn_rose.draw()
            btn_bleu.draw()
            btn_vert.draw()
            btn_orange.draw()
        elif state == "edition":
            edition()

        # Mettre à jour l'affichage
        pygame.display.update()

    pygame.quit()
    sys.exit()

""" ~~~ PARTIE EXECUTIVE : ~~~ """

# Nous commençons ici le main, avec l'appel du main, le reste se fait dans le main (il n'y a pas grand chose ici du coup).


# Appeler la fonction principale main
if __name__ == "__main__":
    main()
