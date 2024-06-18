# --- Le jeu de la vie re-créé par le groupe de TP avec Cuvelier Line, Villeret Baptiste et Besse Fabien  --- #




from tkinter import *
import sys
import pygame
import Structures as St
import Cellule as Cell
import Tableau as Tab
from moviepy.editor import VideoFileClip
import pygame_widgets
from pygame_widgets.button import Button
# Initialisation de Pygame
pygame.init()

# Définir la taille de l'écran selon la taille de la vidéo
screen_width, screen_height = 1100,800
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
MAP_WIDTH, MAP_HEIGHT = 1600, 1200
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
Cette fonction permet d'inverser la couleur d'un pixel 
"""
def inverser_couleur_pixel(x, y):
    if 0 <= y < len(matrice) and 0 <= x < len(matrice[0]):
        matrice[y][x] = 1 - matrice[y][x]

def zoom(event, facteur_zoom):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            facteur_zoom = min(10, facteur_zoom + 1)
        elif event.key == pygame.K_m:
            facteur_zoom = max(1, facteur_zoom - 1)
    return facteur_zoom

def deplacement(camera_x, camera_y, camera_speed, screen_width, screen_height, map_width, map_height):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x = max(camera_x - camera_speed, 0)
    if keys[pygame.K_RIGHT]:
        camera_x = min(camera_x + camera_speed, map_width - screen_width)
    if keys[pygame.K_UP]:
        camera_y = max(camera_y - camera_speed, 0)
    if keys[pygame.K_DOWN]:
        camera_y = min(camera_y + camera_speed, map_height - screen_height)
    return camera_x, camera_y

def jeu():
    global matrice, camera_x, camera_y, facteur_zoom
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("son_jdv2.mp3")
    pygame.mixer.music.play(10, 0.0)
    clock = pygame.time.Clock()

    # Dimensions de l'écran
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Création de la surface pour la carte
    map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))

    # Implémentation d'un bouton :
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

    # Mise à jour de l'état du jeu
    matrice_temp = [row[:] for row in matrice]
    running = True
    while running:
        screen.fill((255, 255, 255))  # Assurez-vous que 'blanc' est défini comme (255, 255, 255)

        # Gestion des événements
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            facteur_zoom = zoom(event, facteur_zoom)

        quitter_2.listen(events)

        # Gestion des touches pour déplacer la caméra
        camera_x, camera_y = deplacement(camera_x, camera_y, camera_speed, screen_width, screen_height, MAP_WIDTH,
                                         MAP_HEIGHT)

        # Dessin de la partie visible de la carte sur la fenêtre
        screen.blit(map_surface, (0, 0), (camera_x, camera_y, screen_width, screen_height))

        # Applications de la fonction règle qui modifie l'état des cellules
        for y in range(len(matrice) - 1):
            for x in range(len(matrice[y]) - 1):
                ma_cell = Cell.Cellule(matrice, y, x, matrice_temp)
                ma_cell.regle()

        # Copie de la matrice
        matrice = [row[:] for row in matrice_temp]

        # Dessin de la grille
        dessiner_grille(map_surface, matrice, facteur_zoom)

        # Dessin du bouton quitter
        quitter_2.draw()

        pygame.display.flip()
        clock.tick(10)  # Limite le jeu à 10 images par seconde

    pygame.quit()
    sys.exit()


def show_menu():
    global state, play, quitter, reg
    state = "menu"
    play = Button(
        screen,  # Surface to place button on
        screen_width // 2 - 150,   # X-coordinate of top left corner
        screen_height // 2 - 250,  # Y-coordinate of top left corner
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
        onClick=edition  # Function to call when clicked on
    )

    quitter = Button(
        screen,  # Surface to place button on
        screen_width // 2 - 150,  # X-coordinate of top left corner
        screen_height // 2 + 150,  # Y-coordinate of top left corner
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
        screen_width // 2 - 150,  # X-coordinate of top left corner
        screen_height // 2 - 50,  # Y-coordinate of top left corner
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

rect_color = (255, 255, 255, 180)  # Blanc avec 50% de transparence
rect_width, rect_height = 980, 860
rect_surface = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA)
rect_surface.fill(rect_color)


def edition():
    global state, matrice, camera_x, camera_y, facteur_zoom, back_to_menu
    state = "edition"
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Définition des polices d'écriture et des textes :
    smallfont = pygame.font.SysFont('Corbel', 20)

    # Variables pour les boutons
    back_to_menu_2 = Button(
        screen,  # Surface to place button on
        screen_width - 590,  # X-coordinate of top left corner
        screen_height - 90,  # Y-coordinate of top left corner
        150,  # Width
        50,  # Height

        # Optional Parameters
        text='MENU',  # Text to display
        fontSize=30,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=40,  # Radius of border corners (leave empty for not curved)
        onClick=show_menu  # Function to call when clicked on
    )
    jeuB = Button(
        screen,  # Surface to place button on
        screen_width - 775,  # X-coordinate of top left corner
        screen_height - 90,  # Y-coordinate of top left corner
        170,  # Width
        50,  # Height

        # Optional Parameters
        text='COMMENCER',  # Text to display
        fontSize=30,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=jeu  # Function to call when clicked on
    )
    #############################Definition des boutons et initialisation des images pour le menu édition#############################
    croix = pygame.image.load("croix.png")
    canoe = pygame.image.load("canoe.png")
    cligno = pygame.image.load("cligno.png")
    hamecon = pygame.image.load("hamecon.png")
    hamecon2 = pygame.image.load("hamecon2.png")
    penntadeca = pygame.image.load("pentadeca.png")
    deuxLapins = pygame.image.load("deux_lapins.png")

    # On définit la nouvelle taille :
    largeur_hauteur_image = (100, 100)
    croix_redim = pygame.transform.scale(croix, largeur_hauteur_image)
    canoe_redim = pygame.transform.scale(canoe, largeur_hauteur_image)
    cligno_redim = pygame.transform.scale(cligno, largeur_hauteur_image)
    hamecon_redim = pygame.transform.scale(hamecon, largeur_hauteur_image)
    hamecon2_redim = pygame.transform.scale(hamecon2, largeur_hauteur_image)
    penntadeca_redim = pygame.transform.scale(penntadeca, largeur_hauteur_image)
    deuxLapins_redim = pygame.transform.scale(deuxLapins, largeur_hauteur_image)

    canoe_btn = Button(
        screen,  # Surface to place button on
        screen_width-275,  # X-coordinate of top left corner
        50,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=canoe_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None # Function to call when clicked on
    )
    croix_btn = Button(
        screen,
        screen_width-125,  # Surface to place button on
        50,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=croix_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None  # Function to call when clicked on
    )
    cligno_btn = Button(
        screen,  # Surface to place button on
        screen_width-275,  # X-coordinate of top left corner
        200,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=cligno_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None  # Function to call when clicked on
    )
    hamecon_btn = Button(
        screen,  # Surface to place button on
        screen_width-125,  # X-coordinate of top left corner
        200,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=hamecon_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None  # Function to call when clicked on
    )
    hamecon2_btn = Button(
        screen,  # Surface to place button on
        screen_width-275,  # X-coordinate of top left corner
        350,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=hamecon2_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None  # Function to call when clicked on
    )
    penntadeca_btn = Button(
        screen,  # Surface to place button on
        screen_width-125,  # X-coordinate of top left corner
        350,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=penntadeca_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None  # Function to call when clicked on
    )
    deuxLapins_btn = Button(
        screen,  # Surface to place button on
        screen_width-275,  # X-coordinate of top left corner
        500,  # Y-coordinate of top left corner
        100,  # Width
        100,  # Height
        image=deuxLapins_redim,
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=None  # Function to call when clicked on
    )

    if state == "menu":
        play.draw()
        quitter.draw()
        reg.draw()
    while state == "edition":
        for event in pygame.event.get():
            back_to_menu_2.listen(pygame.event.get())
            jeuB.listen(pygame.event.get())
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu_2.draw()
                x, y = event.pos
                x = (x + camera_x) // (taille_cellule * facteur_zoom)
                y = (y + camera_y) // (taille_cellule * facteur_zoom)
                inverser_couleur_pixel(x, y)

            facteur_zoom = zoom(event, facteur_zoom)
        camera_x, camera_y = deplacement(camera_x, camera_y, camera_speed, screen_width, screen_height, MAP_WIDTH,MAP_HEIGHT)
        screen.fill((255, 255, 255))
        screen.blit(map_surface, (0, 0), (camera_x, camera_y, screen_width, screen_height))
        dessiner_grille(map_surface, matrice, facteur_zoom)


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
        pygame.display.flip()


    state = "menu"


# Modification de la fonction main pour inclure l'état edition
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
        screen.blit(rect_surface, (0, 0))

        titre = "Le Jeu de la Vie"
        titre_police = font_titre.render(titre, True, noir)
        screen.blit(titre_police, (340, 30))

        if state == "menu":
            play.draw()
            quitter.draw()
            reg.draw()
        elif state == "rules":
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


pygame.mixer.init()
pygame.mixer.music.load("son_jdv.mp3")
pygame.mixer.music.play(10, 0.0)
# Appeler la fonction principale
if __name__ == "__main__":
    main()
