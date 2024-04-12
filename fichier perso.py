class Tableau:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def creation_tableau(self,longueur, largeur):
        #le tableau est une liste de listes pouvant etre parcouru, pour se faire,
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

class Cellule_vivante:
    def __init__(self, matrice, coy, cox):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
    def survie(self):

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
        if matrice[self.coy][self.cox] == 1:
            cmpt = 0
            for i in range(top-1, 2-bottom_or):
                for j in range(left-1, 2-right_or):
                    if matrice[self.coy + i][self.cox + j] == 1:
                        cmpt += 1
            # si la cellule a 3 ou 4 voisines avec elle compris
            if cmpt == 3 or cmpt == 4:
                return matrice
            else:
                matrice[self.coy][self.cox] = 0
                return matrice
        else:
            print(self.cox, " = cox et coy = ", self.coy, matrice[self.coy][self.cox], "matrice")
            return 1


mon_tab = Tableau(10, 8)
matrice = mon_tab.creation_tableau(10, 8)
print("tableau vide")
#for i in range(len(matrice)):
    #for j in range(len(matrice[0])):
ma_cell = Cellule_vivante(matrice, 5, 5)

matrice[4][4]=1
matrice[3][3]=1
matrice[5][5]=1

print("\n")
for i in range(len(matrice)):
    print(matrice[i])
print("tableau modifié")

ma_cell.survie()

print("\n")
for i in range(len(matrice)):
    print(matrice[i])
print("tableau apres la survie")