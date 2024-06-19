colors = [
    (255, 0, 0),    # Rouge
    (0, 255, 0),    # Vert
    (0, 0, 255),    # Bleu
    (255, 255, 0),  # Jaune
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (128, 128, 128),# Gris
    (255, 165, 0),  # Orange
    (0, 128, 0),    # Vert foncé
    (128, 0, 128),  # Violet
    (0, 0, 128),    # Bleu foncé
    (255, 192, 203),# Rose
    (255, 215, 0),  # Or
    (0, 0, 0)       # Noir
]

def choix_couleur():
    couleur_choisie = None  # Initialise couleur_choisie à None
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (320 <= x < 350) and (365 <= y < 395):
                couleur_choisie = colors[0]
            if (350 <= x < 380) and (365 <= y < 395):
                couleur_choisie = colors[1]
            if (380 <= x < 410) and (365 <= y < 395):
                couleur_choisie = colors[2]
            if (410 <= x < 440) and (365 <= y < 395):
                couleur_choisie = colors[3]
            if (440 <= x < 470) and (365 <= y < 395):
                couleur_choisie = colors[4]
            if (470 <= x < 500) and (365 <= y < 395):
                couleur_choisie = colors[5]
            if (500 <= x < 530) and (365 <= y < 395):
                couleur_choisie = colors[6]
            if (320 <= x < 350) and (395 <= y <= 425):
                couleur_choisie = colors[7]
            if (350 <= x < 380) and (395 <= y <= 425):
                couleur_choisie = colors[8]
            if (380 <= x < 410) and (395 <= y <= 425):
                couleur_choisie = colors[9]
            if (410 <= x < 440) and (395 <= y <= 425):
                couleur_choisie = colors[10]
            if (440 <= x < 470) and (395 <= y <= 425):
                couleur_choisie = colors[11]
            if (470 <= x < 500) and (395 <= y <= 425):
                couleur_choisie = colors[12]
            if (500 <= x < 530) and (395 <= y <= 425):
                couleur_choisie = colors[13]
    return couleur_choisie
couleur_choisie=choix_couleur()

def show_parametre():
    global state, retour_menu
    state = "parametre"
    taille_carre = 30
    # Position de départ des premiers carrés
    start_x = (largeur_ecran - 7 * taille_carre) // 2
    start_y = (hauteur_ecran - 2 * taille_carre) // 2 - 100

    # Dessiner les carrés
    for i, color in enumerate(colors):
        row = i // 7
        col = i % 7
        x = start_x + col * taille_carre
        y = start_y + row * taille_carre
        pygame.draw.rect(ecran, color, (x, y, taille_carre, taille_carre))

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
    pygame.display.flip()
    choix_couleur()

###
elif state == "parametre":
show_parametre()
retour_menu.draw()