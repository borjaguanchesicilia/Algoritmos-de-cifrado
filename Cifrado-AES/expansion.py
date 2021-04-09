import numpy as np

def expansionClaves(key, w, nK, nB, nR):

    temp = []
    i = 0

    rCon = ['01000000', '02000000', '04000000', '08000000', '10000000', '20000000', '40000000', '80000000', '1B000000', '36000000']


    while(i < nK): # nk = 4
        w.append((key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]))
        i = i + 1
    
    i = nK
    
    print("La primera clave es: ", w)

    aux1 = aux2 = aux3 = aux4 = 0
    byteRcon = ""

    while(i < nB * (nR+1)): # nB = 4 nR = 10
        temp.append(w[i-1])
        if (i % nK == 0):
            for j in range(4):
                auxGeneral = subWord(rotWord(temp))
                byteRcon = rCon[round(i/nK)-1][0] + rCon[round(i/nK)-1][1]
                aux1 = int(auxGeneral[0], 16) ^ int(byteRcon, 16); byteRcon = ""
                byteRcon = rCon[round(i/nK)-1][2] + rCon[round(i/nK)-1][3]
                aux2 = int(auxGeneral[1], 16) ^ int(byteRcon, 16); byteRcon = ""
                byteRcon = rCon[round(i/nK)-1][4] + rCon[round(i/nK)-1][5]
                aux3 = int(auxGeneral[2], 16) ^ int(byteRcon, 16); byteRcon = ""
                byteRcon = rCon[round(i/nK)-1][6] + rCon[round(i/nK)-1][7]
                aux4 = int(auxGeneral[3], 16) ^ int(byteRcon, 16); byteRcon = ""
            temp = []
            temp.append((hex(aux1)[2:], hex(aux2)[2:], hex(aux3)[2:], hex(aux4)[2:]))
            aux1 = aux2 = aux3 = aux4 = 0
        elif (nK > 6 and i % nK == 4):
            temp = []
            temp.append(subWord(temp))

        aux1 = int(w[i-nK][0], 16) ^ int(temp[0][0], 16)
        aux2 = int(w[i-nK][1], 16) ^ int(temp[0][1], 16)
        aux3 = int(w[i-nK][2], 16) ^ int(temp[0][2], 16)
        aux4 = int(w[i-nK][3], 16) ^ int(temp[0][3], 16)
        w.append((hex(aux1)[2:], hex(aux2)[2:], hex(aux3)[2:], hex(aux4)[2:]))
        aux1 = aux2 = aux3 = aux4 = 0
        i = i + 1
        temp = []

    subClaves = []
    subClave = ""
    aux1 = aux2 = aux3 = aux4 = ""
    for i in range(0, 44, 4):
        aux1 = w[i][0] + w[i][1] + w[i][2] + w[i][3]
        aux2 = w[i+1][0] + w[i+1][1] + w[i+1][2] + w[i+1][3]
        aux3 = w[i+2][0] + w[i+2][1] + w[i+2][2] + w[i+2][3]
        aux4 = w[i+3][0] + w[i+3][1] + w[i+3][2] + w[i+3][3]
        subClave = aux1 + aux2 + aux3 + aux4
        subClaves.append(subClave)
        subClave = ""
        aux1 = aux2 = aux3 = aux4 = ""

    print(subClaves)
    return subClaves
        
def subWord(bytes):

    sCaja = np.loadtxt('sCaja.txt',dtype=str)

    matrizResultado = []

    aux1 = aux2 = 0

    for i in range(len(bytes)):
        aux1 = int(bytes[i][0], 16)
        if len(bytes[i]) < 2:
            aux2 = int(bytes[i][0], 16)
            aux1 = 0
        else:
            aux2 = int(bytes[i][1], 16)

        matrizResultado.append(str(sCaja[aux1][aux2]))

    return matrizResultado


def rotWord(bytes):

    matrizResultado = []

    matrizResultado.append(bytes[0][1])
    matrizResultado.append(bytes[0][2])
    matrizResultado.append(bytes[0][3])
    matrizResultado.append(bytes[0][0])

    return matrizResultado