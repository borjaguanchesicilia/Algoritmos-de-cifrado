# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 09/04/2021
# File funciones.py: Implementación de funciones auxiliares para el cifrado AES.


def matrizToString(matriz):

    cadena = ""
    for i in range(len(matriz)):
        cadena = cadena + matriz[i]

    return cadena


def traspuesta(matriz):
    
    matrizResultado = []

    for i in range(4):
        matrizResultado.append(matriz[i])
        matrizResultado.append(matriz[i+4])
        matrizResultado.append(matriz[i+8])
        matrizResultado.append(matriz[i+12])

    return matrizResultado


def cadenaToMatrizBytes(cadena):
    
    matriz = []
    str = ""

    for i in range(0, len(cadena), 2):
        aux = cadena[i] + cadena[i+1]
        byte = hex(int(aux, 16))[2:]
        if len(byte) == 1:
            byte = "0" + byte
        matriz.append(byte)
        aux = ""

    return matriz