def cligno(matrice, cox, coy):
    for i in range(3):
        matrice[coy+i][cox] = 1
    return matrice

def hamecon(matrice, cox, coy):
    for i in range(3):
        matrice[coy+i][cox] = 1
    matrice[coy][cox-1] = 1
    matrice[coy+3][cox+1] = 1
    matrice[coy+3][cox+2] = 1
    matrice[coy+2][cox+2] = 1
    return matrice
def hamecon2(matrice, cox, coy):
    for i in range(5):
        matrice[coy-i-1][cox+i] = 1
    for i in range(6):
        matrice[coy-i][cox+i] = 1
    matrice[coy-1][cox+1] = 0
    matrice[coy-4][cox+4] = 0
    matrice[coy-3][cox+2] = 0
    matrice[coy][cox+1] = 1
    matrice[coy-2][cox+3] = 1
    matrice[coy-4][cox+5] = 1
    return matrice


def canoe(matrice, cox, coy):
    for i in range(4):
        matrice[coy+i+1][cox+i] = 1
    matrice[coy][cox] = 1
    matrice[coy][cox+1] = 1
    matrice[coy+4][cox+4] = 1
    matrice[coy+3][cox+4] = 1

def penntadeca(matrice, cox, coy):
    for i in range(10):
        matrice[coy][cox + i] = 1
    matrice[coy][cox + 2] = 0
    matrice[coy][cox + 7] = 0
    matrice[coy + 1][cox + 2] = 1
    matrice[coy - 1][cox + 2] = 1
    matrice[coy + 1][cox + 7] = 1
    matrice[coy - 1][cox + 7] = 1
    return matrice

def croix(matrice, cox, coy):
    for i in range(4):
        matrice[coy][cox+i+2] = 1
        matrice[coy+7][cox+i+2] = 1
        matrice[coy+2+i][cox] = 1
        matrice[coy+i+2][cox+7] = 1
    for j in range(6):
        matrice[coy + 2][cox + 1 + j] = 1
        matrice[coy + 5][cox + 1 + j] = 1
    for k in range(2):
        matrice[coy + 2][cox + 3 + k] = 0
        matrice[coy + 5][cox + 3 + k] = 0
    for l in range(0, 5, 3):
        matrice[coy + 1][cox + 2 + l] = 1
        matrice[coy + 6][cox + 2 + l] = 1

def  deuxLapins(matrice, cox, coy):
    matrice[coy + 1][cox] = 1
    matrice[coy + 1][cox + 2] = 1
    matrice[coy][cox + 4] = 1
    matrice[coy][cox + 6] = 1
    matrice[coy + 1][cox + 5] = 1
    matrice[coy + 2][cox + 5] = 1
    matrice[coy + 2][cox + 1] = 1
    matrice[coy + 3][cox + 1] = 1
    matrice[coy + 3][cox + 7] = 1