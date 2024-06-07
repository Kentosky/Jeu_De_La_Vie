import pygame

# Initialisation des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
couleur_contour = (0, 0, 0)  # La couleur du contour (noir dans cet exemple)


def dessiner_grille(map_surface, matrice, taille_cellule):
    for y in range(len(matrice)):
        for x in range(len(matrice[0])):
            # Détermination de la couleur de remplissage
            couleur = blanc if matrice[y][x] == 0 else noir

            # Création du rectangle de la cellule
            rect_cellule = pygame.Rect(x * taille_cellule, y * taille_cellule, taille_cellule, taille_cellule)

            # Dessin du carré rempli
            pygame.draw.rect(map_surface, couleur, rect_cellule)

            # Dessin du contour du carré
            pygame.draw.rect(map_surface, couleur_contour, rect_cellule, 1)


# Exemple d'utilisation
pygame.init()
taille_cellule = 20
matrice = [[0, 1], [1, 0]]
largeur, hauteur = len(matrice[0]) * taille_cellule, len(matrice) * taille_cellule
map_surface = pygame.display.set_mode((largeur, hauteur))

dessiner_grille(map_surface, matrice, taille_cellule)
pygame.display.flip()

# Garder la fenêtre ouverte pendant 3 secondes pour voir le résultat
pygame.time.wait(3000)
pygame.quit()
