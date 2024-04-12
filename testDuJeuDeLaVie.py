class vide:
    def __init__(self, matrice, cox, coy):
        self.cox = cox
        self.coy = coy
        self.matrice = matrice
    def lookfornaissance(self, matrice, cox, coy):
        if matrice[cox][coy] == 0:
            cmpt = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if matrice[cox + i][coy + j] == 1:
                        cmpt += 1
            if cmpt == 3:
                return 1
            else:
                return 0
        else:
            print(cox, " = cox et coy = ", coy, matrice[cox][coy], "matrice")
            return 1

tableau_de_tableaux = []
for i in range(5):
    ligne = []
    for j in range(5):
        ligne.append(0)
    tableau_de_tableaux.append(ligne)

print(tableau_de_tableaux)
for i in range(3):
    tableau_de_tableaux[i][2] = 1

print(tableau_de_tableaux)
print(tableau_de_tableaux[1][3])

case = vide(tableau_de_tableaux, 1, 2)
print(case.lookfornaissance(matrice=tableau_de_tableaux, cox=1, coy=2))

