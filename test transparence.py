import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button

# Initialiser Pygame
pygame.init()

# Définir les dimensions de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bouton Image')

# Charger et redimensionner l'image
button_image = pygame.image.load('canoe.png')
button_image = pygame.transform.scale(button_image, (150, 50))  # Redimensionner l'image à 150x50 pixels

# Définir les couleurs
noir = (0, 0, 0)

def show_menu():
    print("Menu affiché")

def image_clicked():
    print("Image cliquée!")

# Créer un bouton avec une image
back_to_menu = Button(
    screen,  # Surface to place button on
    screen_width - 170,  # X-coordinate of top left corner
    screen_height - 70,  # Y-coordinate of top left corner
    150,  # Width
    50,  # Height

    # Optional Parameters
    text='',  # Pas de texte car on utilise une image
    fontSize=30,  # Taille de la police (inutile ici)
    margin=20,  # Distance minimale entre le texte/image et le bord du bouton
    inactiveColour=(0, 0, 0, 0),  # Couleur du bouton quand il n'est pas interactif (transparent)
    hoverColour=(0, 0, 0, 0),  # Couleur du bouton quand il est survolé (transparent)
    pressedColour=(0, 0, 0, 0),  # Couleur du bouton quand il est cliqué (transparent)
    radius=20,  # Rayon des coins du bord (laisser vide pour pas arrondi)
    onClick=image_clicked,  # Fonction à appeler lors du clic
    image=button_image  # Image à afficher sur le bouton
)

def main():
    running = True
    while running:  # Boucle principale
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Mettez à jour les widgets de Pygame
            pygame_widgets.update(event)

        # Remplir l'écran avec une couleur de fond
        screen.fill((255, 255, 255))

        # Dessiner le bouton
        back_to_menu.draw()

        # Mettre à jour l'affichage
        pygame.display.update()

    pygame.quit()
    sys.exit()

main()
