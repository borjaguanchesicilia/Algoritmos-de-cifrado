import numpy as np
from expansion import *
from operaciones import *


def aes(clave, textoEnClaro):

    fichero = open('ejecuciones.txt',"w") # Fichero para almacenar todas los resultados de las operaciones

    MatrizDeEstado = []
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
        MatrizDeEstado.append(suma)

    MatrizDeEstadoString = matrizToString(MatrizDeEstado)

    print("R0  (Subclave =", claves[0], ") = ", MatrizDeEstadoString)
    j = j + 1


    # Resto de rondas

    for i in range(9):
        fichero.write("La clave es: ")
        fichero.write(str(claves[j]))
        fichero.write("\n")
        fichero.write("La Matriz de estado es: ")
        fichero.write(str(MatrizDeEstado))
        fichero.write("\n\n")

        # Operación SubBytes
        MatrizDeEstado = operacionSustitucion(MatrizDeEstado, sCaja)
        fichero.write("Operacion sustitucion: ")
        fichero.write(str(MatrizDeEstado))
        fichero.write("\n\n")

        # Operación de ShiftRow
        MatrizDeEstado = operacionDesplazamiento(MatrizDeEstado)
        fichero.write("Operacion desplazamiento: ")
        fichero.write(str(MatrizDeEstado))
        fichero.write("\n\n")

        # Operación de MixColumn
        MatrizDeEstado = operacionMultiplicacion(MatrizDeEstado)
        fichero.write("Operacion multiplicacion: ")
        fichero.write(str(MatrizDeEstado))
        fichero.write("\n\n")

        # Operación de AddRoundKey
        MatrizDeEstado = operacionSuma(cadenaToMatrizBytes(claves[j]), MatrizDeEstado)
        fichero.write("Operacion suma: ")
        fichero.write(str(MatrizDeEstado))
        fichero.write("\n\n\n\n")

        MatrizDeEstadoString = matrizToString(MatrizDeEstado)
        print("R%d" %(i+1), " (Subclave =", claves[j], ") = ", MatrizDeEstadoString)
        j = j + 1


    # Última ronda

    fichero.write("La clave es: ")
    fichero.write(str(claves[j]))
    fichero.write("\n")
    fichero.write("La Matriz de estado es: ")
    fichero.write(str(MatrizDeEstado))
    fichero.write("\n\n")

    # Operación SubBytes
    MatrizDeEstado = operacionSustitucion(MatrizDeEstado, sCaja)
    fichero.write("Operacion sustitucion: ")
    fichero.write(str(MatrizDeEstado))
    fichero.write("\n\n")
    
    # Operación de ShiftRow
    MatrizDeEstado = operacionDesplazamiento(MatrizDeEstado)
    fichero.write("Operacion desplazamiento: ")
    fichero.write(str(MatrizDeEstado))
    fichero.write("\n\n")
    
    # Operación de AddRoundKey
    MatrizDeEstado = operacionSuma(cadenaToMatrizBytes(claves[j]), MatrizDeEstado)
    fichero.write("Operacion suma: ")
    fichero.write(str(MatrizDeEstado))
    fichero.write("\n\n")
    
    MatrizDeEstadoString = matrizToString(MatrizDeEstado)
    print("R10 (Subclave =", claves[j], ") = ", MatrizDeEstadoString)