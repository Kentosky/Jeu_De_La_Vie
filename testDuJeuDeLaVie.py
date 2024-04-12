class vide:
    def __init__(self, matrice, cox, coy):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
    def lookfornaissance(self, matrice, cox, coy):

        left = 0
        top = 0
        cmpt = 0
        bottom_OOR = 0
        right_OOR = 0

        right = len(matrice[0])
        bottom = len(matrice)

        if cox == 0:
            left = 1

        if coy == 0:
            top = 1

        if coy == bottom:
            bottom_OOR += 1

        if cox == right:
            right_OOR += 1

        if matrice[coy][cox] == 0:

            for i in range(top-1, 2-bottom_OOR, 1):
                for j in range(left-1, 2-right_OOR, 1):

                    if matrice[coy + i][cox + j] == 1:
                        cmpt += 1
                        print("oui !")
            if cmpt == 3:
                matrice[coy][cox] = 1
                return matrice

            else:
                return matrice

        elif matrice[coy][cox] == 1:
            return matrice

tableau_de_tableaux = []
for i in range(5):
    ligne = []
    for j in range(5):
        ligne.append(0)
    tableau_de_tableaux.append(ligne)

for i in range(1, 4, 1):
    tableau_de_tableaux[i][2] = 1

len(tableau_de_tableaux)
print(tableau_de_tableaux)

case = vide(tableau_de_tableaux, 3, 1)
print(case.lookfornaissance(matrice=tableau_de_tableaux, cox=3, coy=2))