class Tableau:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def creation_tableau(longueur, largeur):
        # creer le quadrillage
        tableau_de_tableaux = []
        for i in range(largeur):
            ligne = []
            for j in range(longueur):
                ligne.append(0)
            tableau_de_tableaux.append(ligne)

        # Afficher le quadrillage
        for ligne in tableau_de_tableaux:
            print(ligne)
        return tableau_de_tableaux





