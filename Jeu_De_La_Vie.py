
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
from moviepy.editor import VideoFileClip
import pygame_widgets
from pygame_widgets.button import Button

largeur_ecran = 800
hauteur_ecran = 600
taille_cellule = 5
x_matrice = int(largeur_ecran/taille_cellule)
y_matrice = int(largeur_ecran/taille_cellule)
#définition des couleurs :
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
blanc = (255, 255, 255)
noir = (0, 0, 0)
couleur_bordure = (224, 224, 224)

facteur_zoom = 5
izoom = 1
zoom_max = 10
zoom_min = 1

couleur_curseur = (150, 150, 150)
curseur_largeur = 10
curseur_longueur = 50
# Création d'une surface pour la carte
MAP_WIDTH, MAP_HEIGHT = 1600, 1200
map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
# Position initiale de la caméra centrée
camera_x = (MAP_WIDTH - largeur_ecran) // 2
camera_y = (MAP_HEIGHT - hauteur_ecran) // 2
camera_speed = 20

# Initialisation de Pygame
pygame.init()

# Définir la taille de l'écran selon la taille de la vidéo
screen_width, screen_height = 1100, 800
screen = pygame.display.set_mode((screen_width, screen_height))
video = VideoFileClip("video.mp4").resize((1600,800))
pygame.display.set_caption("Video du menu")


# Définir la police
font = pygame.font.Font('Tiny5-regular.ttf', size = 25)

""" ~~~ PARTIE FONCTIONNELLE ~~~ """

""" ~~~  PARTIE MENU D'INTRO  ~~~ """

def edition():
    global matrice
    pygame.quit()
    pygame.init()
    ecran_edition = pygame.display.set_mode((largeur_ecran+200, hauteur_ecran))


    #définition des polices d'écriture et des textes :
    smallfont = pygame.font.SysFont('Corbel',20)
    confirmer = smallfont.render('confirmer' , True , blanc)
    quitter = smallfont.render('quitter' , True , blanc)
    suivant = smallfont.render('suivant' , True , blanc)
    precedent = smallfont.render('précédent' , True , blanc)
    #fin variables des boutons--------------------------------------------------
    Mise_en_place_jeu = True
    while Mise_en_place_jeu:
        '''
        Cette boucle va servir à la mise en place du jeu : on génère une matrice vide, donc une grille blanche.
        Ensuite, l'utilisateur survole et clique sur les cases pour les faire changer de couleur. La matrice se met à jour en même temps.
        Une fois le bouton "confirmer" cliqué : la boucle s'arrête et la fenêtre se ferme.
        On passe à la fenêtre suivante.
        '''
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                jeu_en_cours = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    facteur_zoom = min(zoom_max, facteur_zoom + izoom)
                elif event.key == pygame.K_m:
                    facteur_zoom = max(zoom_min, facteur_zoom - izoom)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # mise à jour de la position de la souris
                x = (x + camera_x) // (taille_cellule * facteur_zoom)
                y = (y + camera_y) // (taille_cellule * facteur_zoom)
                inverser_couleur_pixel(x, y)  # utilisation de la fonction inverser_couleur_pixel
                print(matrice)  # test de la mise à jour de la matrice

                if largeur_ecran / 2 - largeur_ecran / 6 <= mouse[0] <= largeur_ecran / 2 + largeur_ecran / 6 and hauteur_ecran - 40 <= mouse[1] <= hauteur_ecran:
                    Mise_en_place_jeu = False
                    break
        # Gestion des touches pour déplacer la caméra
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera_x = max(camera_x - camera_speed, 0)
        if keys[pygame.K_RIGHT]:
            camera_x = min(camera_x + camera_speed, MAP_WIDTH - largeur_ecran)
        if keys[pygame.K_UP]:
            camera_y = max(camera_y - camera_speed, 0)
        if keys[pygame.K_DOWN]:
            camera_y = min(camera_y + camera_speed, MAP_HEIGHT - hauteur_ecran)
        # Efface l'écran avant de dessiner les nouveaux éléments
        ecran_edition.fill(blanc)
        # Dessin de la partie visible de la carte sur la fenêtre
        ecran_edition.blit(map_surface, (0, 0), (camera_x, camera_y, largeur_ecran, hauteur_ecran))
        # Dessiner le quadrillage
        dessiner_grille(map_surface, matrice, facteur_zoom)
        # Dessiner le rectangle gris par-dessus le quadrillage
        pygame.draw.rect(ecran_edition, (170, 170, 170), [largeur_ecran, 0, 200, hauteur_ecran])

        # Mise en place des boutons
        if largeur_ecran / 2 - largeur_ecran / 6 <= mouse[0] <= largeur_ecran / 2 + largeur_ecran / 6 and hauteur_ecran - 40 <= mouse[1] <= hauteur_ecran:
            pygame.draw.rect(ecran_edition, color_light,
                             [largeur_ecran / 2 - largeur_ecran / 6, hauteur_ecran - 40, largeur_ecran / 3, 40])
        else:
            pygame.draw.rect(ecran_edition, color_dark,
                             [largeur_ecran / 2 - largeur_ecran / 6, hauteur_ecran - 40, largeur_ecran / 3, 40])
        # Mise en place du texte des boutons
        ecran_edition.blit(confirmer, (largeur_ecran / 2 - largeur_ecran / 17, hauteur_ecran - 30))
        # Rafraîchissement de la page
        pygame.display.flip()
    pygame.quit()
    pygame.init()
    # Création de la fenêtre
    ecran_jeu = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
    pygame.display.set_caption("Jeu de la Vie")
    clock = pygame.time.Clock()
    # Mise à jour de l'état du jeu
    matrice_temp = [row[:] for row in matrice]
    running = True
    while running:
        ecran_jeu.fill(blanc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    facteur_zoom = min(zoom_max, facteur_zoom + izoom)
                elif event.key == pygame.K_m:
                    facteur_zoom = max(zoom_min, facteur_zoom - izoom)

        # Gestion des touches pour déplacer la caméra
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera_x = max(camera_x - camera_speed, 0)
        if keys[pygame.K_RIGHT]:
            camera_x = min(camera_x + camera_speed, MAP_WIDTH - largeur_ecran)
        if keys[pygame.K_UP]:
            camera_y = max(camera_y - camera_speed, 0)
        if keys[pygame.K_DOWN]:
            camera_y = min(camera_y + camera_speed, MAP_HEIGHT - hauteur_ecran)
        # Dessin de la partie visible de la carte sur la fenêtre
        ecran_jeu.blit(map_surface, (0, 0), (camera_x, camera_y, largeur_ecran, hauteur_ecran))
        pygame.display.flip()
        #applications de la fonctions règle qui modifie l'état des cellules
        for y in range(len(matrice)-1):
            for x in range(len(matrice[y])-1):
                ma_cell = Cell.Cellule(matrice, y, x, matrice_temp)
                ma_cell.regle()
        #copie de la matrice
        matrice = [row[:] for row in matrice_temp]
        # Dessin de la grille
        dessiner_grille(map_surface, matrice, facteur_zoom)
        pygame.time.delay(1)
        pygame.display.flip()
        clock.tick(10)  # Limite le jeu à 10 images par seconde
    pygame.quit()
    sys.exit()

def show_menu():
    global state, play, quitter, reg
    state = "menu"
    play = Button(
        screen,  # Surface to place button on
        screen_width / 2 - 150,   # X-coordinate of top left corner
        screen_height / 2 - 250,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='JOUER',  # Text to display
        fontSize=69,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(0, 100, 60),  # Colour of button when not being interacted with
        hoverColour=(50, 150, 112),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda:edition
    )

    quitter = Button(
        screen,  # Surface to place button on
        screen_width / 2 - 150,  # X-coordinate of top left corner
        screen_height / 2 + 150,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='QUITTER',  # Text to display
        fontSize=69,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: quit()  # Function to call when clicked on
    )

    reg = Button(
        screen,  # Surface to place button on
        screen_width / 2 - 150,  # X-coordinate of top left corner
        screen_height / 2 - 50,  # Y-coordinate of top left corner
        300,  # Width
        100,  # Height

        # Optional Parameters
        text='RÈGLES',  # Text to display
        fontSize=69,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=show_rules  # Function to call when clicked on
    )

def show_rules():
    global state, back_to_menu
    state = "rules"
    back_to_menu = Button(
        screen,  # Surface to place button on
        screen_width - 170,  # X-coordinate of top left corner
        screen_height - 70,  # Y-coordinate of top left corner
        150,  # Width
        50,  # Height

        # Optional Parameters
        text='MENU',  # Text to display
        fontSize=30,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=show_menu  # Function to call when clicked on
    )

def main():
    global state
    show_menu()  # Afficher le menu principal
    state = "menu"

    running = True
    video_start_time = pygame.time.get_ticks()
    while running:  # Boucle principale

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame_widgets.update(event)  # Gestion des événements Pygame et des widgets


        # Calculer le temps écoulé depuis le début de la vidéo
        elapsed_time = (pygame.time.get_ticks() - video_start_time) / 1000

        # Obtenir l'image actuelle de la vidéo
        frame = video.get_frame(elapsed_time)

        # Convertir l'image en surface Pygame
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        # Calculer les coordonnées pour centrer la vidéo
        video_width, video_height = frame_surface.get_size()
        x = (screen_width - video_width) // 2 - 80
        y = (screen_height - video_height) // 2

        # Afficher l'image
        screen.blit(frame_surface, (x, y))

        if state == "menu":
            play.draw()
            quitter.draw()
            reg.draw()
        elif state == "rules":
            # Afficher le texte des règles
            rules_text = [
                "Le jeu de la vie : des règles simples, une infinité de résolutions.","","Le jeu de la vie c’est 2 règles : Règle de survie, règle de naissance. ","","Au début vous devrez choisir la taille du tableau puis la remplir comme vous le souhaitez, ","par la suite, vous verrez le développement des cellules*.","A savoir que si une cellule* ne survie pas, elle meurt.","*cellule = case pleine","","","Règle de survie : ","Si une cellule est entourée de plus d’1 cellule et de moins de 4 cellules, elle survie au prochain ","tour.","","Règle de naissance :","Si une case vide est entourée de exactement 3 cases, alors elle sera vivante le tour d’après."
            ]
            y_offset = 8
            for line in rules_text:
                text_surface = font.render(line, True, noir)
                screen.blit(text_surface, (70, y_offset))
                y_offset += 45

            # Dessiner le bouton pour revenir au menu
            back_to_menu.draw()

        # Mettre à jour l'affichage
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Appeler la fonction principale


""" ~~~ PARTIE EXECUTIVE ~~~ """
#fenetre 1 : explications des règles du jeu.

main()

#fenêtre 2 : choix des pixels colorés sous forme de boutons
#utiles pour test ----
tab1=Tab.Tableau(x_matrice, y_matrice)
matrice = tab1.creation_tableau()
#-------
def dessiner_grille(ecran, matrice, facteur_zoom):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else noir
            rect_cellule = pygame.Rect(x * taille_cellule * facteur_zoom,
                                        y * taille_cellule * facteur_zoom,
                                        taille_cellule * facteur_zoom,
                                        taille_cellule * facteur_zoom)
            pygame.draw.rect(ecran, couleur, rect_cellule)
            pygame.draw.rect(ecran, couleur_bordure, rect_cellule, 1)

# Fonction pour inverser la couleur d'une cellule de la grille
def inverser_couleur_pixel(x, y):
    if 0 <= y < len(matrice) and 0 <= x < len(matrice[0]):
        matrice[y][x] = 1 - matrice[y][x]