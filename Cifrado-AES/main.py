from aes import *

def main(claveString, textoEnClaroString):

    clave = []
    textoEnClaro = []

    clave = cadenaToMatrizBytes(claveString)
    textoEnClaro = cadenaToMatrizBytes(textoEnClaroString)

    aes(clave, textoEnClaro)


def cadenaToMatrizBytes(cadena):

    matriz = []
    str = ""

    for i in range(0, len(cadena), 2):
        str = str + cadena[i] + cadena[i+1]
        matriz.append(hex(int(str, 16)))
        str = ""

    return matriz

#clave = input("Introduzca la clave: ")
#textoEnClaro = input("Introduzca el texto en claro: ")
#clave = "000102030405060708090a0b0c0d0e0f"
#textoEnClaro = "00112233445566778899aabbccddeeff"
clave = "2b7e151628aed2a6abf7158809cf4f3c"
textoEnClaro = "3243f6a8885a308d313198a2e0370734"

main(clave, textoEnClaro)