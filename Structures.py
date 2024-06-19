def cligno(matrice, cox, coy):
    for i in range(18):
        matrice[coy + 9 + i][cox + 7] = 1
        matrice[coy + 28 - (9 + i)][cox + 26 - 7] = 1
    for i in range(11):
        matrice[coy + 9 + i][cox + 13] = 1
    for i in range(9):
        matrice[coy + 8 + i][cox] = 1
        matrice[coy +28 - (8 + i)][cox+26] = 1
    for i in range(5):
        matrice[coy + 9 + 2 * i][cox + 10] = 1
        matrice[coy + 16 + i][cox + 7] = 0
        matrice[coy + 28 - (9 + 2 * i)][cox + 26 - 10] = 1
        matrice[coy + 28 - (16 + i)][cox +26 - 7] = 0
    for i in range(4):
        matrice[coy + 19 + i][cox + 2] = 1
        matrice[coy + 28 - (19 + i)][cox + 26 - 2] = 1
    for i in range(3):
        matrice[coy + 3][cox + 12 + i] = 1
        matrice[coy + 23 + i][cox + 12] = 1
        matrice[coy + 22 + i][cox + 5] = 1
        matrice[coy + 20 + i][cox + 3] = 1
        matrice[coy + 8][cox + 1 + i] = 1
        matrice[coy + 16][cox + 1 + i] = 1
        matrice[coy + i + 11][cox] = 0
        matrice[coy + 12 + i][cox + 9 + i] = 1
        matrice[coy + 28 - 3][cox + 26 - (12 + i)] = 1
        matrice[coy + 28 - (23 + i)][cox + 26 - 12] = 1
        matrice[coy + 28 - (22 + i)][cox + 26 - 5] = 1
        matrice[coy + 28 - (20 + i)][cox + 26 - 3] = 1
        matrice[coy + 28 - 8][cox + 26 - (1 + i)] = 1
        matrice[coy + 28 - 16][cox + 26 - (1 + i)] = 1
        matrice[coy + 28 - (i + 11)][cox + 26] = 0
        matrice[coy + 28 - (12 + i)][cox + 26 - (9 + i)] = 1
    for i in range(2):
        matrice[coy + 28 - (22 + 2 * i)][cox + 26 - 11] = 1
        matrice[coy + 28 - (26 + i)][cox + 26 - 8] = 1
        matrice[coy + 28 - (21 + i)][cox + 26 - 9] = 1
        matrice[coy + 28 - (23 + i)][cox + 26 - 10] = 1
        matrice[coy + 28 - (15 + i)][cox + 26 - 9] = 1
        matrice[coy + 28 - (16 + i)][cox + 26 - 11] = 1
        matrice[coy + 28 - (8 + i)][cox + 26 - 9] = 1
        matrice[coy + 28 - (8 + i)][cox + 26 - 11] = 1
        matrice[coy + 28 - (5 + i)][cox + 26 - 10] = 1
        matrice[coy + 28 - 12][cox + 26 - (9 + 2 * i)] = 1
        matrice[coy + 22 + 2 * i][cox + 11] = 1
        matrice[coy + 26 + i][cox + 8] = 1
        matrice[coy + 21 + i][cox + 9] = 1
        matrice[coy + 23 + i][cox + 10] = 1
        matrice[coy + 15 + i][cox + 9] = 1
        matrice[coy + 16 + i][cox + 11] = 1
        matrice[coy + 8 + i][cox + 9] = 1
        matrice[coy + 8 + i][cox + 11] = 1
        matrice[coy + 5 + i][cox + 10] = 1
        matrice[coy + 12][cox + 9 + 2 * i] = 1
        for j in range(0, 8, 2):
            matrice[coy + 9 + j][cox + 4 + i] = 1
            matrice[coy + 28 - (9 + j)][cox + 26 - (4 + i)] = 1
    matrice[coy + 11][cox + 1] = 1
    matrice[coy + 13][cox + 1] = 1
    matrice[coy + 19][cox + 1] = 1
    matrice[coy + 10][cox + 6] = 1
    matrice[coy + 14][cox + 6] = 1
    matrice[coy + 20][cox + 4] = 1
    matrice[coy + 20][cox + 6] = 1
    matrice[coy + 20][cox + 10] = 1
    matrice[coy + 19][cox + 12] = 1
    matrice[coy + 24][cox + 4] = 1
    matrice[coy + 25][cox + 6] = 1
    matrice[coy + 7][cox + 12] = 1
    matrice[coy + 4][cox + 11] = 1
    matrice[coy + 26][cox + 9] = 1
    matrice[coy + 28 - 11][cox + 26 - 1] = 1
    matrice[coy + 28 - 13][cox + 26 - 1] = 1
    matrice[coy + 28 - 19][cox + 26 - 1] = 1
    matrice[coy + 28 - 10][cox + 26 - 6] = 1
    matrice[coy + 28 - 14][cox + 26 - 6] = 1
    matrice[coy + 28 - 20][cox + 26 - 4] = 1
    matrice[coy + 28 - 20][cox + 26 - 6] = 1
    matrice[coy + 28 - 20][cox + 26 - 10] = 1
    matrice[coy + 28 - 19][cox + 26 - 12] = 1
    matrice[coy + 28 - 24][cox + 26 - 4] = 1
    matrice[coy + 28 - 25][cox + 26 - 6] = 1
    matrice[coy + 28 - 7][cox + 26 - 12] = 1
    matrice[coy + 28 - 4][cox + 26 - 11] = 1
    matrice[coy + 28 - 26][cox + 26 - 9] = 1
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

def spacefiller(matrice, cox, coy):
    for i in range(18):
        matrice[coy + 9 + i][cox + 7] = 1
        matrice[coy + 28 - (9 + i)][cox + 26 - 7] = 1
    for i in range(11):
        matrice[coy + 9 + i][cox + 13] = 1
    for i in range(9):
        matrice[coy + 8 + i][cox] = 1
        matrice[coy + 28 - (8 + i)][cox + 26] = 1
    for i in range(5):
        matrice[coy + 9 + 2 * i][cox + 10] = 1
        matrice[coy + 16 + i][cox + 7] = 0
        matrice[coy + 28 - (9 + 2 * i)][cox + 26 - 10] = 1
        matrice[coy + 28 - (16 + i)][cox + 26 - 7] = 0
    for i in range(4):
        matrice[coy + 19 + i][cox + 2] = 1
        matrice[coy + 28 - (19 + i)][cox + 26 - 2] = 1
    for i in range(3):
        matrice[coy + 3][cox + 12 + i] = 1
        matrice[coy + 23 + i][cox + 12] = 1
        matrice[coy + 22 + i][cox + 5] = 1
        matrice[coy + 20 + i][cox + 3] = 1
        matrice[coy + 8][cox + 1 + i] = 1
        matrice[coy + 16][cox + 1 + i] = 1
        matrice[coy + i + 11][cox] = 0
        matrice[coy + 12 + i][cox + 9 + i] = 1
        matrice[coy + 28 - 3][cox + 26 - (12 + i)] = 1
        matrice[coy + 28 - (23 + i)][cox + 26 - 12] = 1
        matrice[coy + 28 - (22 + i)][cox + 26 - 5] = 1
        matrice[coy + 28 - (20 + i)][cox + 26 - 3] = 1
        matrice[coy + 28 - 8][cox + 26 - (1 + i)] = 1
        matrice[coy + 28 - 16][cox + 26 - (1 + i)] = 1
        matrice[coy + 28 - (i + 11)][cox + 26] = 0
        matrice[coy + 28 - (12 + i)][cox + 26 - (9 + i)] = 1
    for i in range(2):
        matrice[coy + 28 - (22 + 2 * i)][cox + 26 - 11] = 1
        matrice[coy + 28 - (26 + i)][cox + 26 - 8] = 1
        matrice[coy + 28 - (21 + i)][cox + 26 - 9] = 1
        matrice[coy + 28 - (23 + i)][cox + 26 - 10] = 1
        matrice[coy + 28 - (15 + i)][cox + 26 - 9] = 1
        matrice[coy + 28 - (16 + i)][cox + 26 - 11] = 1
        matrice[coy + 28 - (8 + i)][cox + 26 - 9] = 1
        matrice[coy + 28 - (8 + i)][cox + 26 - 11] = 1
        matrice[coy + 28 - (5 + i)][cox + 26 - 10] = 1
        matrice[coy + 28 - 12][cox + 26 - (9 + 2 * i)] = 1
        matrice[coy + 22 + 2 * i][cox + 11] = 1
        matrice[coy + 26 + i][cox + 8] = 1
        matrice[coy + 21 + i][cox + 9] = 1
        matrice[coy + 23 + i][cox + 10] = 1
        matrice[coy + 15 + i][cox + 9] = 1
        matrice[coy + 16 + i][cox + 11] = 1
        matrice[coy + 8 + i][cox + 9] = 1
        matrice[coy + 8 + i][cox + 11] = 1
        matrice[coy + 5 + i][cox + 10] = 1
        matrice[coy + 12][cox + 9 + 2 * i] = 1
        for j in range(0, 8, 2):
            matrice[coy + 9 + j][cox + 4 + i] = 1
            matrice[coy + 28 - (9 + j)][cox + 26 - (4 + i)] = 1
    matrice[coy + 11][cox + 1] = 1
    matrice[coy + 13][cox + 1] = 1
    matrice[coy + 19][cox + 1] = 1
    matrice[coy + 10][cox + 6] = 1
    matrice[coy + 14][cox + 6] = 1
    matrice[coy + 20][cox + 4] = 1
    matrice[coy + 20][cox + 6] = 1
    matrice[coy + 20][cox + 10] = 1
    matrice[coy + 19][cox + 12] = 1
    matrice[coy + 24][cox + 4] = 1
    matrice[coy + 25][cox + 6] = 1
    matrice[coy + 7][cox + 12] = 1
    matrice[coy + 4][cox + 11] = 1
    matrice[coy + 28 - 11][cox + 26 - 1] = 1
    matrice[coy + 28 - 13][cox + 26 - 1] = 1
    matrice[coy + 28 - 19][cox + 26 - 1] = 1
    matrice[coy + 28 - 10][cox + 26 - 6] = 1
    matrice[coy + 28 - 14][cox + 26 - 6] = 1
    matrice[coy + 28 - 20][cox + 26 - 4] = 1
    matrice[coy + 28 - 20][cox + 26 - 6] = 1
    matrice[coy + 28 - 20][cox + 26 - 10] = 1
    matrice[coy + 28 - 19][cox + 26 - 12] = 1
    matrice[coy + 28 - 24][cox + 26 - 4] = 1
    matrice[coy + 28 - 25][cox + 26 - 6] = 1
    matrice[coy + 28 - 7][cox + 26 - 12] = 1
    matrice[coy + 28 - 4][cox + 26 - 11] = 1