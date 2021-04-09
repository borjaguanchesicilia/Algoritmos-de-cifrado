from auxiliar import *
from multiplicacion import *

def operacionSustitucion(matriz, sCaja):

    matrizResultado = []

    aux1 = aux2 = 0

    for i in range(len(matriz)):
        aux1 = int(matriz[i][0], 16)
        if len(matriz[i]) < 2:
            aux2 = int(matriz[i][0], 16)
            aux1 = 0
        else:
            aux2 = int(matriz[i][1], 16)

        matrizResultado.append(str(sCaja[aux1][aux2]))

    return matrizResultado


def operacionDesplazamiento(matriz):
    
    matrizFinal = []
    matrizAux = []

    matrizAux = traspuesta(matriz)

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

    matrizFinal = traspuestaInv(matrizFinal)

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

    for i in range(16):
        suma = hex(int(clave[i], 16) ^ int(matriz[i], 16))[2:]
        if len(suma) != 2:
            suma = "0" + suma
        matrizResultado.append(suma)

    return matrizResultado