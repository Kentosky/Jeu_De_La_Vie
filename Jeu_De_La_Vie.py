# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #

import sys
import pygame

import Structures
import Cellule as Cell
import Tableau as Tab
from moviepy.editor import VideoFileClip
import pygame_widgets
from pygame_widgets.button import Button
# Initialisation de Pygame
pygame.init()

# Définir la taille de l'écran selon la taille de la vidéo
screen_width, screen_height = 1100, 800
screen = pygame.display.set_mode((screen_width, screen_height))
# In resize.py line 37 : change "ANTIALIAS" by "LANCZOS"
video = VideoFileClip("video.mp4").resize((1600,800))
pygame.display.set_caption("Video du menu")

# Création de notre tableau a partir de la classe Tableau
taille_cellule = 5
x_matrice = int(screen_width/taille_cellule)
y_matrice = int(screen_width/taille_cellule)
tab1=Tab.Tableau(x_matrice, y_matrice)
matrice = tab1.creation_tableau()

#définition des couleurs que nous utiliserons :
blanc = (255, 255, 255)
noir = (0, 0, 0)
couleur_bordure = (224, 224, 224)

#variable de zoom
facteur_zoom = 5

# Création d'une surface pour la carte
MAP_WIDTH, MAP_HEIGHT = 3200, 2400
map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))

# Position initiale de la caméra centrée
camera_x = (MAP_WIDTH - screen_width) // 2
camera_y = (MAP_HEIGHT - screen_height) // 2
camera_speed = 20 # vitesse de déplacement de la camera

# Définition la police
font = pygame.font.Font('Tiny5-regular.ttf', size = 25)
font_titre = pygame.font.Font('Tiny5-regular.ttf', size = 70)

"""
Cette fonction permet de dessiner une grille pygame à partir de la matrice que l'on a créé précedemment
De base, chaque case de la grille est un carré blanc qui est cliquable et qui changera de couleur par la suite
"""
def dessiner_grille(ecran, matrice, facteur_zoom):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            couleur = blanc if matrice[y][x] == 0 else noir
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
def deplacement(camera_x, camera_y, camera_speed, screen_width, screen_height, map_width, map_height):
    keys = pygame.key.get_pressed()
    # deplacement selon la flèche gauche
    if keys[pygame.K_LEFT]:
        camera_x = max(camera_x - camera_speed, 0)
    # deplacement selon la flèche droite
    if keys[pygame.K_RIGHT]:
        camera_x = min(camera_x + camera_speed, map_width - screen_width)
    # deplacement selon la flèche haute
    if keys[pygame.K_UP]:
        camera_y = max(camera_y - camera_speed, 0)
    # deplacement selon la flèche basse
    if keys[pygame.K_DOWN]:
        camera_y = min(camera_y + camera_speed, map_height - screen_height)
    return camera_x, camera_y

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
        screen,  # Surface to place button on
        screen_width - 120,  # X-coordinate of top left corner
        screen_height - 60,  # Y-coordinate of top left corner
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
    menu_2= Button(
        screen,  # Surface to place button on
        screen_width - 230,  # X-coordinate of top left corner
        screen_height - 60,  # Y-coordinate of top left corner
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
        screen.fill((255, 255, 255))

        # Gestion des événements
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # Gestion du zoom avec appel de la fonction
            facteur_zoom = zoom(event, facteur_zoom)
        #bouton quitter
        quitter_2.listen(events)
        menu_2.listen(events)

        # Gestion du déplacement avec appel de la fonction
        camera_x, camera_y = deplacement(camera_x, camera_y, camera_speed, screen_width, screen_height, MAP_WIDTH,MAP_HEIGHT)
        # Dessin de la partie visible de la carte sur la fenêtre
        screen.blit(map_surface, (0, 0), (camera_x, camera_y, screen_width, screen_height))

        # Applications de la fonction règle qui modifie l'état des cellules
        for y in range(len(matrice) - 1):
            for x in range(len(matrice[y]) - 1):
                # Création de toutes les cellules présentes sur la map et application des règles
                ma_cell = Cell.Cellule(matrice, y, x, matrice_temp)
                ma_cell.regle()

        # Copie de la matrice
        matrice = [row[:] for row in matrice_temp]
        # Dessin de la grille
        dessiner_grille(map_surface, matrice, facteur_zoom)
        # Dessin du bouton quitter
        quitter_2.draw()
        menu_2.draw()

        # Mise à jour de la fenetre
        pygame.display.flip()
        clock.tick(10)  # Limite le jeu à 10 images par seconde

    pygame.quit()
    sys.exit()

"""
Cette fonction est la fonction de menu:
Celle-ci affiche 3 boutons (Jouer, Règles et Quitter)
"""
def show_menu():
    global state, play, quitter, reg
    state = "menu"
    # Création du bouton Jouer
    play = Button(
        screen,  # ecran choisi
        screen_width // 2 - 150,   # coordonnes x bouton
        screen_height // 2 - 250,  # coordonnes y bouton
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
        screen,  # Surface sur laquelle placer le bouton
        screen_width // 2 - 150,  # Coordonnée x du coin supérieur gauche
        screen_height // 2 + 150,  # Coordonnée y du coin supérieur gauche
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
    reg = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width // 2 - 150,  # Coordonnée x du coin supérieur gauche
        screen_height // 2 - 50,  # Coordonnée y du coin supérieur gauche
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

"""
Cette fonction est la fonction de règles:
Celle-ci affiche les règles du jeu pour le joueur 
"""
def show_rules():
    global state, back_to_menu
    state = "rules"
    # Création du bouton Retour au Menu
    back_to_menu = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 170,  # Coordonnée x du coin supérieur gauche
        screen_height - 70,  # Coordonnée y du coin supérieur gauche
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


rect_color = (255, 255, 255, 180)  # Blanc avec 50% de transparence
rect_width, rect_height = 980, 860
rect_surface = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA)
rect_surface.fill(rect_color)

def rst():
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
    global state, matrice, camera_x, camera_y, facteur_zoom, back_to_menu
    state = "edition"
    pygame.init()

    # Variables pour les boutons
    # Création du bouton Retour au Menu 2
    back_to_menu_2 = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 465,  # Coordonnée x du coin supérieur gauche
        screen_height - 90,  # Coordonnée y du coin supérieur gauche
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
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 650,  # Coordonnée x du coin supérieur gauche
        screen_height - 90,  # Coordonnée y du coin supérieur gauche
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
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 860,  # Coordonnée x du coin supérieur gauche
        screen_height - 90,  # Coordonnée y du coin supérieur gauche
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
        onClick=rst  # Fonction à appeler lors du clic
    )

    #############################Definition des boutons et initialisation des images pour le menu édition#############################
    #Importation des images au format png
    croix = pygame.image.load("croix.png")
    canoe = pygame.image.load("canoe.png")
    cligno = pygame.image.load("cligno.png")
    hamecon = pygame.image.load("hamecon.png")
    hamecon2 = pygame.image.load("hamecon2.png")
    penntadeca = pygame.image.load("pentadeca.png")
    deuxLapins = pygame.image.load("deux_lapins.png")

    # On définit la nouvelle taille de l'image afin que toutes aient la même taille :
    largeur_hauteur_image = (100, 100)

    # On redimensionne chaque image
    croix_redim = pygame.transform.scale(croix, largeur_hauteur_image)
    canoe_redim = pygame.transform.scale(canoe, largeur_hauteur_image)
    cligno_redim = pygame.transform.scale(cligno, largeur_hauteur_image)
    hamecon_redim = pygame.transform.scale(hamecon, largeur_hauteur_image)
    hamecon2_redim = pygame.transform.scale(hamecon2, largeur_hauteur_image)
    penntadeca_redim = pygame.transform.scale(penntadeca, largeur_hauteur_image)
    deuxLapins_redim = pygame.transform.scale(deuxLapins, largeur_hauteur_image)

    # Création du bouton Canoë
    canoe_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 275,  # Coordonnée x du coin supérieur gauche
        50,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=canoe_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Croix
    croix_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 125,  # Coordonnée x du coin supérieur gauche
        50,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=croix_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Clignotant
    cligno_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 275,  # Coordonnée x du coin supérieur gauche
        200,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=cligno_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Hameçon
    hamecon_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 125,  # Coordonnée x du coin supérieur gauche
        200,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=hamecon_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Hameçon 2
    hamecon2_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 275,  # Coordonnée x du coin supérieur gauche
        350,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=hamecon2_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Penntadeca
    penntadeca_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 125,  # Coordonnée x du coin supérieur gauche
        350,  # Coordonnée y du coin supérieur gauche
        100,  # Largeur
        100,  # Hauteur
        image=penntadeca_redim,  # Image du bouton
        radius=20,  # Rayon pour arrondir les coins du bouton
        onClick=None  # Fonction à appeler lors du clic
    )

    # Création du bouton Deux Lapins
    deuxLapins_btn = Button(
        screen,  # Surface sur laquelle placer le bouton
        screen_width - 275,  # Coordonnée x du coin supérieur gauche
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
        surface_texte = font.render("Insertion : " + cdc, True, noir,(125, 255, 175))
        rect_texte = surface_texte.get_rect()
        rect_texte.center = ((screen_width - 300)// 2, 50)
        # Affichage du texte
        screen.blit(surface_texte, rect_texte)

    #Mise en place des modes de dessin : drawing = False tant que le second clic n'a pas été fait.
    #Quand on clique sur le Canva après avoir cliqué sur une image de forme prédéfinie, drawing = True :
    #On peut maintenant placer la figure aux coordonnées sur lesquelles nous cliquons.
    drawing = False
    drawing_canoe=False
    drawing_croix=False
    drawing_cligno=False
    drawing_hamecon=False
    drawing_hamecon2=False
    drawing_penntadeca=False
    drawing_deuxLapins=False


    if state == "menu":
        play.draw()
        quitter.draw()
        reg.draw()
    # tant qu'on est dans l'état édition :
    while state == "edition":
        for event in pygame.event.get():
            back_to_menu_2.listen(pygame.event.get())               #On met à jour régulièrement l'état du bouton back_to_menu_2
            jeuB.listen(pygame.event.get())
            reini.listen(pygame.event.get())
            if event.type == pygame.QUIT:
                pygame.quit()                                       #La fenêtre se ferme et le programme s'arrête si le bouton quitter est cliqué
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu_2.draw()                               #On place le bouton back_to_menu_2
                x, y = event.pos                                    #on relève les coordonnées de la souris

                '''A partir de cette ligne : 
                On met en place les conditions pour savoir quelle image afficher lorsque l'on clique sur une image
                représentant une forme prédéfinie.'''
                #Si on appuie dans la zone correspondant au bouton Canoe :
                if (screen_width-275 <= x <= screen_width-175) and (50 <= y <= 150) :
                    if event.button == 1 :
                        if not drawing:                             # Ce premier clic prépare le placement du rectangle
                            drawing_canoe = True
                            break                                   # On arrête la boucle pour ne pas entrer dans les autres conditions if


                # Si on appuie dans la zone correspondant au bouton Croix :
                elif (screen_width-125 <= x <= screen_width-25) and (50 <= y <= 150) :
                    if event.button == 1 :
                        if not drawing:
                            drawing_croix = True
                            break

                # Si on appuie dans la zone correspondant au bouton Cligno :
                elif (screen_width-275 <= x <= screen_width-175) and (200 <= y <= 300) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_cligno = True
                            break

                # Si on appuie dans la zone correspondant au bouton Hameçon :
                elif (screen_width-125 <= x <= screen_width-25) and (200 <= y <= 300) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_hamecon = True
                            break

                # Si on appuie dans la zone correspondant au bouton Hameçon 2 :
                elif (screen_width-275 <= x <= screen_width-175) and (350 <= y <= 450) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_hamecon2 = True
                            break

                # Si on appuie dans la zone correspondant au bouton Penta décathlon:
                elif (screen_width-125 <= x <= screen_width-25) and (350 <= y <= 450) :
                    if event.button == 1 :
                        if not drawing:
                            # Premier clic pour préparer le placement de l'image
                            drawing_penntadeca = True
                            break

                # Si on appuie dans la zone correspondant au bouton Deux Lapins :
                elif (screen_width-275 <= x <= screen_width-175) and (500 <= y <= 600) :
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
                        break

                    if drawing_croix == True :                              #On réitère le même procédé avec la figure Croix
                        x, y = convertir_pos_matrice(x, y)
                        Structures.croix(matrice, x, y)
                        drawing_croix=False
                        drawing = False
                        break

                    if drawing_cligno == True :
                        x, y = convertir_pos_matrice(x, y)
                        Structures.cligno(matrice, x, y)
                        drawing_cligno=False
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



                x, y = convertir_pos_matrice(x, y)                          #Si aucun if n'est lan
                inverser_couleur_pixel(x, y)
                # Dessiner le rectangle
                pygame.display.flip()


            facteur_zoom = zoom(event, facteur_zoom)
        camera_x, camera_y = deplacement(camera_x, camera_y, camera_speed, screen_width, screen_height, MAP_WIDTH,MAP_HEIGHT)
        screen.fill((255, 255, 255))
        screen.blit(map_surface, (0, 0), (camera_x, camera_y, screen_width, screen_height))
        dessiner_grille(map_surface, matrice, facteur_zoom)

        if drawing_canoe:
            mode_actif("Canoe")
        if drawing_croix:
            mode_actif("Croix")
        if drawing_cligno:
            mode_actif("Cligno")
        if drawing_hamecon:
            mode_actif("Hameçon")
        if drawing_hamecon2:
            mode_actif("Hameçon 2")
        if drawing_penntadeca:
            mode_actif("Pentadecathlon")
        if drawing_deuxLapins:
            mode_actif("Deux Lapins")

        pygame.draw.rect(screen, (170, 170, 170), [screen_width - 300, 0, 300, screen_height])

        canoe_btn.draw()
        croix_btn.draw()
        cligno_btn.draw()
        hamecon_btn.draw()
        hamecon2_btn.draw()
        penntadeca_btn.draw()
        deuxLapins_btn.draw()

        jeuB.draw()
        back_to_menu_2.draw()
        reini.draw()
        pygame.display.flip()


    state = "menu"


# Modification de la fonction main pour inclure l'état edition
def main():
    global state
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
        x = (screen_width - video_width) // 2 - 80
        y = (screen_height - video_height) // 2

        # Afficher l'image
        screen.blit(frame_surface, (x, y))
        screen.blit(rect_surface, (0, 0))

        titre = "Le Jeu de la Vie"
        titre_police = font_titre.render(titre, True, noir)
        screen.blit(titre_police, (340, 30))

        if state == "menu":         # Condition pour revenir au menu
            play.draw()
            quitter.draw()
            reg.draw()
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
                text_surface = font.render(line, True, noir)
                screen.blit(text_surface, (70, y_offset))
                y_offset += 40

            # Dessiner le bouton pour revenir au menu
            back_to_menu.draw()
        elif state == "edition":
            edition()

        # Mettre à jour l'affichage
        pygame.display.update()

    pygame.quit()
    sys.exit()

""" ~~~ PARTIE EXECUTIVE : ~~~ """

# Nous commençons ici le main, avec l'appel du main, le reste se fait dans le main (il n'y a pas grand chose ici du coup).

pygame.mixer.init()                             # Initialisation du mixer pour la musique in game
pygame.mixer.music.load("son_jdv.mp3")          # Load du son trop cool
pygame.mixer.music.play(10, 0.0)     # Lancement de la musique (elle se répetera 10 fois

# Appeler la fonction principale main
if __name__ == "__main__":
    main()
