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
        for ligne in tableau_de_tableaux:       #ici, on affiche la liste de listes pour la vérification
            print(ligne)
        return tableau_de_tableaux

class Cellule:
    def __init__(self, matrice, coy, cox, temp_matrice):      # dans cet ordre car on cree les colones avant les lignes
        self.cox = cox                          # coordonnée x
        self.coy = coy                          # coordonnée y
        self.matrice = matrice                  # matrice
        # on créé une matrice temporaire pour pouvoir faire tous les déplacements sans risquer un effet domino
        self.temp_matrice = temp_matrice

    def regle(self):
        # on gère d'abord le cas où la cellule est collé a un coté du quadrillage
        left = top = right_or = bottom_or = 0
        right = len(self.matrice[0])
        bottom = len(self.matrice)

        if self.cox == left:
            left += 1
        if self.cox == right:
            right_or += 1
        if self.coy == top:
            top += 1
        if self.coy == bottom:
            bottom_or += 1

        # on gère maintenant la survie de la cellule
        if self.matrice[self.coy][self.cox] == 1:                       # 1er cas: la cellule est vivante
            cmptS = 0                                                   # compteur de voisins
            for i in range(top - 1, 2 - bottom_or):                     # on regarde autour de la cellule
                for j in range(left - 1, 2 - right_or):                 #               |
                    if self.matrice[self.coy + i][self.cox + j] == 1:   # si une voisine est vivante
                        cmptS += 1                                      # on incrémente le compteur de voisins

            if cmptS == 3 or cmptS == 4:                                # si la cellule a 2 ou 3 voisines (compteur=3 ou 4 car elle se compte elle-même)
                self.temp_matrice[self.coy][self.cox] = 1               # rien ne se passe, la cellule reste en vie

            else:
                self.temp_matrice[self.coy][self.cox] = 0               # sinon la cellule meurt, on modifie son état

        else:                                                           # 2eme cas:la cellule est morte
            cmptN = 0                                                   # compteur de voisins
            for i in range(top - 1, 2 - bottom_or, 1):                  # on regarde autour de la voisine
                for j in range(left - 1, 2 - right_or, 1):              #               |
                    if self.matrice[self.coy + i][self.cox + j] == 1:   # si une voisine est vivante
                        cmptN += 1                                      # on incrémente le compteur
            if cmptN == 3:                                              # si la cellule a 3 voisines (compteur=4 car elle se compte elle-même)
                self.temp_matrice[self.coy][self.cox] = 1               # la cellule meurt, on modifie son état

            else:
                self.temp_matrice[self.coy][self.cox] = 0               # sinon rien ne se passe, la cellule reste morte

        return self.temp_matrice


############################# MAIN #############################

print("Création du tableau")
mon_tab = Tableau(10, 8)
matrice = mon_tab.creation_tableau()


matrice[3][3] = 1
matrice[3][4] = 1
matrice[3][5] = 1

print("\nTableau modifié avec l'ajout de cellules vivantes :")
for ligne in matrice:
    print(ligne)

matrice_temp = [row[:] for row in matrice]

#applications de la fonctions règle qui modifie l'état des cellules
for y in range(len(matrice)-1):
    for x in range(len(matrice[y])-1):
        ma_cell = Cellule(matrice, y, x, matrice_temp)
        ma_cell.regle()

#copie de la matrice
matrice = [row[:] for row in matrice_temp]
print("\nmatrice apres modifications :")
for row in matrice:
    print(row)

