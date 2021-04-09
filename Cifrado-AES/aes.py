import numpy as np
from multiplicacion import *


def aes(clave, textoEnClaro):

    claveString = matrizToString(clave)

    bloque = []

    # Recogida de la sCaja

    sCaja = np.loadtxt('sCaja.txt',dtype=str)


    # Ronda inicial

    for i in range(len(textoEnClaro)):
        bloque.append(hex(int(clave[i], 16) ^ int(textoEnClaro[i], 16)))

    bloqueString = matrizToString(bloque)

    print("R0 (Subclave = ", claveString, ") = ", bloqueString)

    bloque = operacionSustitucion(bloque, sCaja)
    print("Operacion sustitucion: ", bloque)
    bloque = operacionDesplazamiento(bloque)
    print("Operacion desplazamiento: ", bloque)
    bloque = operacionMultiplicacion(bloque)
    print("Operacion multiplicacion: ", bloque)
    clave = ['a0', 'fa', 'fe', '17', '88', '54', '2c', 'b1', '23', 'a3', '39', '39', '2a', '6e', '76', '05']
    bloque = operacionSuma(clave, bloque)
    print("Operacion suma: ", bloque)

    # Resto de rondas


def operacionSustitucion(matriz, sCaja):

    matrizResultado = []

    aux1 = aux2 = 0

    for i in range(len(matriz)):
        aux1 = int(matriz[i][2], 16)
        if len(matriz[i]) < 4:
            aux2 = int(matriz[i][2], 16)
            aux1 = 0
        else:
            aux2 = int(matriz[i][3], 16)

        matrizResultado.append(str(sCaja[aux1][aux2]))

    return matrizResultado


def operacionDesplazamiento(matriz):
    
    matrizFinal = []
    matrizAux = []

    matrizAux = recolocar(matriz)

    matrizFinal.append(matrizAux[0])
    matrizFinal.append(matrizAux[1])
    matrizFinal.append(matrizAux[2])
    matrizFinal.append(matrizAux[3])
    
    desplz = 1

    for i in range(1, len(matriz)):
        if desplz == 1:
            matrizFinal.append(matriz[i+4])
            matrizFinal.append(matriz[i+8])
            matrizFinal.append(matriz[i+12])
            matrizFinal.append(matriz[i])
            desplz = desplz + 1
        elif desplz == 2:
            matrizFinal.append(matriz[i+8])
            matrizFinal.append(matriz[i+12])
            matrizFinal.append(matriz[i])
            matrizFinal.append(matriz[i+4])
            desplz = desplz + 1
        elif desplz == 3:
            matrizFinal.append(matriz[i+12])
            matrizFinal.append(matriz[i])
            matrizFinal.append(matriz[i+4])
            matrizFinal.append(matriz[i+8])
            desplz = desplz + 1
            break

    matrizFinal = recolocarInv(matrizFinal)

    return matrizFinal


def operacionMultiplicacion(matriz):

    matrizResultado = []

    s0 = s1 = s2 = s3 = 0

    multip02 = bytesABinario(int("02", 16))
    multip03 = bytesABinario(int("03", 16))

    for i in range(0, 16, 4):
        multiplicacion1 = multiplicacion(multip02, bytesABinario(int(matriz[i], 16)), "00011011")
        multiplicacion2 = multiplicacion(multip03, bytesABinario(int(matriz[i+1], 16)), "00011011")
        s0 = int(multiplicacion1, 16) ^ int(multiplicacion2, 16) ^ int(matriz[i+2], 16) ^ int(matriz[i+3], 16)
        
        multiplicacion1 = int(multiplicacion(multip02, bytesABinario(int(matriz[i+1], 16)), "00011011"), 16)
        multiplicacion2 = int(multiplicacion(multip03, bytesABinario(int(matriz[i+2], 16)), "00011011"), 16)
        s1 = int(matriz[i], 16) ^ multiplicacion1 ^ multiplicacion2 ^ int(matriz[i+3], 16)
        
        multiplicacion1 = int(multiplicacion(multip02, bytesABinario(int(matriz[i+2], 16)), "00011011"), 16)
        multiplicacion2 = int(multiplicacion(multip03, bytesABinario(int(matriz[i+3], 16)), "00011011"), 16)
        s2 = int(matriz[i], 16) ^ int(matriz[i+1], 16) ^ multiplicacion1 ^ multiplicacion2 
        
        multiplicacion1 = int(multiplicacion(multip03, bytesABinario(int(matriz[i], 16)), "00011011"), 16)
        multiplicacion2 = int(multiplicacion(multip02, bytesABinario(int(matriz[i+3], 16)), "00011011"), 16)
        s3 =  multiplicacion1 ^ int(matriz[i+1], 16) ^ int(matriz[i+2], 16) ^ multiplicacion2


        matrizResultado.append(hex(s0)[2:])
        matrizResultado.append(hex(s1)[2:])
        matrizResultado.append(hex(s2)[2:])
        matrizResultado.append(hex(s3)[2:])
        s0 = s1 = s2 = s3 = 0

    return matrizResultado


def operacionSuma(clave, matriz):

    matrizResultado = []

    for i in range(len(matriz)):
        matrizResultado.append(hex(int(clave[i], 16) ^ int(matriz[i], 16))[2:])

    return matrizResultado


def expansionClaves(key, w, nK):

    temp = 0
    i = 0

    while(i < nK):
        w[i] = (key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
        i = i + 1
    
    i = nK


    while(i < nB * (nR+1)):
        temp = w[i-1]
        if (i % nK == 0):
            temp = subWord(rotWord(temp)) ^ rCon[i/nK]
        elif (nK > 6 and i % nK == 4):
            temp = subWord(temp)

        w[i] = w[i-nK] ^ temp
        i = i + 1

def matrizToString(matriz):

    cadena = ""
    for i in range(len(matriz)):
        cadena = cadena + matriz[i]

    cadena = cadena.replace("0x", "")

    return cadena


def recolocar(matriz):
    
    matrizResultado = []

    for i in range(4):
        matrizResultado.append(matriz[i])
        matrizResultado.append(matriz[i+4])
        matrizResultado.append(matriz[i+8])
        matrizResultado.append(matriz[i+12])

    return matrizResultado


def recolocarInv(matriz):
    
    matrizResultado = []

    matrizResultado.append(matriz[0])
    matrizResultado.append(matriz[4])
    matrizResultado.append(matriz[8])
    matrizResultado.append(matriz[12])

    for i in range(1, 4):
        matrizResultado.append(matriz[i])
        matrizResultado.append(matriz[i+4])
        matrizResultado.append(matriz[i+8])
        matrizResultado.append(matriz[i+12])

    return matrizResultado