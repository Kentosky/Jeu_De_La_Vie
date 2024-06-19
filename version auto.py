import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Dimensions de l'écran
largeur_ecran = 800
hauteur_ecran = 600

# Initialisation de la couleur du bouton enregistrée
couleur_enregistree = None

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Boutons interactifs avec Pygame")

# Classe Bouton
class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte = texte

    def afficher(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)
        petit_texte = pygame.font.Font(None, 36)
        texte_surface = petit_texte.render(self.texte, True, BLANC)
        texte_rect = texte_surface.get_rect(center=self.rect.center)
        ecran.blit(texte_surface, texte_rect)

    def est_clique(self, pos_souris):
        return self.rect.collidepoint(pos_souris)

# Création des boutons
bouton_rouge = Bouton(50, 50, 200, 100, ROUGE, "Rouge")
bouton_vert = Bouton(300, 50, 200, 100, VERT, "Vert")
bouton_bleu = Bouton(550, 50, 200, 100, BLEU, "Bleu")

boutons = [bouton_rouge, bouton_vert, bouton_bleu]

# Boucle principale
while True:
    ecran.fill(BLANC)  # Fond de l'écran en blanc

    # Affichage des boutons
    for bouton in boutons:
        bouton.afficher(ecran)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                pos_souris = pygame.mouse.get_pos()
                for bouton in boutons:
                    if bouton.est_clique(pos_souris):
                        couleur_enregistree = bouton.couleur  # Enregistrer la couleur du bouton cliqué
                        print(f"Couleur enregistrée : {couleur_enregistree}")

    pygame.display.flip()  # Mettre à jour l'écran
    pygame.time.Clock().tick(60)  # Limiter le nombre de FPS
