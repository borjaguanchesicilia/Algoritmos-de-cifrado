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
        str = str + cadena[i] + cadena[i+1]
        matriz.append(hex(int(str, 16))[2:])
        str = ""

    return matriz