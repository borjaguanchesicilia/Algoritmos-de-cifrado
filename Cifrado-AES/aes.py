import numpy as np
from multiplicacion import *
from expansion import *


def aes(clave, textoEnClaro):

    fichero = open('ejecuciones.txt',"w") # Fichero para almacenar todas los resultados de las operaciones

    bloque = []
    nK = nB = 4 # Tamaño de 
    nR = 10 # Número de rondas
    aux = ""
    w = []
    j = 0 # Clave que se usará


    # Recogida de la sCaja desde fichero y cargada como matriz
    sCaja = np.loadtxt('sCaja.txt',dtype=str)


    # Expansión de la clave (se obtienen 10 subclaves)
    claves = expansionClaves(clave, w, nK, nB, nR)


    # Ronda inicial

    byteClave = ""
    for i in range(0, 32, 2):
        byteClave = claves[j][i] + claves[j][i+1]
        byteTextoEnClaro = textoEnClaro[i] + textoEnClaro[i+1]
        suma = hex(int(byteClave, 16) ^ int(byteTextoEnClaro, 16))[2:]
        if len(suma) != 2:
            suma = "0" + suma
        bloque.append(suma)

    bloqueString = matrizToString(bloque)

    print("R0  (Subclave =", claves[0], ") = ", bloqueString)
    j = j + 1

    # Resto de rondas

    for i in range(9):
        fichero.write("La clave es: ")
        fichero.write(str(claves[j]))
        fichero.write("\n")
        fichero.write("El bloque es: ")
        fichero.write(str(bloque))
        fichero.write("\n\n")

        # Operación SubBytes
        bloque = operacionSustitucion(bloque, sCaja)
        fichero.write("Operacion sustitucion: ")
        fichero.write(str(bloque))
        fichero.write("\n\n")

        # Operación de ShiftRow
        bloque = operacionDesplazamiento(bloque)
        fichero.write("Operacion desplazamiento: ")
        fichero.write(str(bloque))
        fichero.write("\n\n")

        # Operación de MixColumn
        bloque = operacionMultiplicacion(bloque)
        fichero.write("Operacion multiplicacion: ")
        fichero.write(str(bloque))
        fichero.write("\n\n")

        # Operación de AddRoundKey
        bloque = operacionSuma(cadenaToMatrizBytes(claves[j]), bloque)
        fichero.write("Operacion suma: ")
        fichero.write(str(bloque))
        fichero.write("\n\n\n\n")

        bloqueString = matrizToString(bloque)
        print("R%d" %(i+1), " (Subclave =", claves[j], ") = ", bloqueString)
        j = j + 1


    # Última ronda

    fichero.write("La clave es: ")
    fichero.write(str(claves[j]))
    fichero.write("\n")
    fichero.write("El bloque es: ")
    fichero.write(str(bloque))
    fichero.write("\n\n")

    # Operación SubBytes
    bloque = operacionSustitucion(bloque, sCaja)
    fichero.write("Operacion sustitucion: ")
    fichero.write(str(bloque))
    fichero.write("\n\n")
    
    # Operación de ShiftRow
    bloque = operacionDesplazamiento(bloque)
    fichero.write("Operacion desplazamiento: ")
    fichero.write(str(bloque))
    fichero.write("\n\n")
    
    # Operación de AddRoundKey
    bloque = operacionSuma(cadenaToMatrizBytes(claves[j]), bloque)
    fichero.write("Operacion suma: ")
    fichero.write(str(bloque))
    fichero.write("\n\n")
    
    bloqueString = matrizToString(bloque)
    print("R10 (Subclave =", claves[j], ") = ", bloqueString)


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

    for i in range(16):
        suma = hex(int(clave[i], 16) ^ int(matriz[i], 16))[2:]
        if len(suma) != 2:
            suma = "0" + suma
        matrizResultado.append(suma)

    return matrizResultado


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


def cadenaToMatrizBytes(cadena):
    
    matriz = []
    str = ""

    for i in range(0, len(cadena), 2):
        str = str + cadena[i] + cadena[i+1]
        matriz.append(hex(int(str, 16))[2:])
        str = ""

    return matriz