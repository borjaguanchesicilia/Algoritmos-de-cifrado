# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 09/04/2021
# File aes.py: Implementación del cifrado AES.


import numpy as np
from expansion import *
from operaciones import *


def aes(clave, textoEnClaro):

    fichero = open('ejecuciones.txt',"w") # Fichero para almacenar todas los resultados de las operaciones

    MatrizDeEstado = []
    nK = nB = 4 # Tamaño de 
    nR = 10 # Número de rondas
    aux = ""
    j = 0 # Clave que se usará


    # Recogida de la sCaja desde fichero y cargada como matriz
    sCaja = np.loadtxt('sCaja.txt',dtype=str)


    # Expansión de la clave (se obtienen 10 subclaves)
    claves = expansionClaves(clave, nK, nB, nR)


    # Ronda inicial

    MatrizDeEstado = operacionSuma(cadenaToMatrizBytes(claves[j]), textoEnClaro)
    MatrizDeEstadoString = matrizToString(MatrizDeEstado)

    print("\n\nR0  (Subclave =", claves[0], ") = ", MatrizDeEstadoString)
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
    print("\n\nEl bloque de texto cifrado es: ", MatrizDeEstadoString)

    return MatrizDeEstado