class Tableau:
    """ Classe qui permet de créer une liste de listes qui sera ensuite interprété comme toutes les cases du jeu de la vie. """
    def __init__(self, longueur, largeur):      # Initialisation
        self.longueur = longueur
        self.largeur = largeur
    def creation_tableau(self):                 #fonction principale permettant de créer la liste de liste
        # creer le quadrillage
        tableau_de_tableaux = []
        for i in range(self.largeur):           #la liste de listes fera une largeur de la variable largeur
            ligne = []
            for j in range(self.longueur):      #la liste de listes fera une longueur de la variable longueur
                ligne.append(0)
            tableau_de_tableaux.append(ligne)

        # Afficher le quadrillage

        return tableau_de_tableaux