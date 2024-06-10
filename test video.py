import pygame
import moviepy
from moviepy.editor import *
#-------
largeur_ecran = 800
hauteur_ecran_sans_boutons = 500
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

sensibilite_zomm = 0.1
izoom = 0.1
zoom_max = 5.0
zoom_min = 0.1

couleur_curseur = (150, 150, 150)
curseur_largeur = 10
curseur_longueur = 50

pygame.init()
video = moviepy.editor.VideoFileClip("video.mp4")
video.preview()

jeu_en_cours = True

while jeu_en_cours:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            jeu_en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:                                                     # Molette vers le haut
                facteur_zoom += izoom
            elif event.button == 5:                                                   # Molette vers le bas
                facteur_zoom = max(zoom_min, facteur_zoom - izoom)
            else:
                x, y = event.pos                                                      #mise à jour de la position de la souris
                x = (x - decalage_x) // (taille_cellule * facteur_zoom)
                y = (y - decalage_y) // (taille_cellule * facteur_zoom)
                inverser_couleur_pixel(x, y)                                          #utilisation de la fonction inverser_couleur_pixel
                print(matrice)                                                        #test de la mise à jour de la matrice

        if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                   # Si on clique la souris sur le bouton confirmer cela ferme la fenêtre
            if largeur_ecran / 2 - largeur_ecran / 6 <= mouse[0] <= largeur_ecran / 2 + largeur_ecran / 6 and hauteur_ecran -40 <= mouse[1] <= hauteur_ecran :
                jeu_en_cours = False
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

                                                  #La couleur du bouton change si il est survolé par la souris
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
