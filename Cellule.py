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