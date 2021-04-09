# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 09/04/2021
# File main.py Recogida del texto en claro y de la clave


from aes import *

def main(claveString, textoEnClaroString):

    clave = []

    for i in range(0, len(claveString), 2):
        aux = claveString[i] + claveString[i+1]
        byte = hex(int(aux, 16))[2:]
        if len(byte) == 1:
            byte = "0" + byte
        clave.append(byte)
        aux = ""

    aes(clave, textoEnClaroString)

#clave = input("Introduzca la clave: ")
#textoEnClaro = input("Introduzca el texto en claro: ")
clave = "000102030405060708090a0b0c0d0e0f"
textoEnClaro = "00112233445566778899aabbccddeeff"
#clave = "2b7e151628aed2a6abf7158809cf4f3c"
#textoEnClaro = "3243f6a8885a308d313198a2e0370734"

main(clave, textoEnClaro)