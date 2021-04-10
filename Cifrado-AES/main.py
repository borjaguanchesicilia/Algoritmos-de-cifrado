# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 09/04/2021
# File main.py Recogida del texto en claro y de la clave


from aes import *

def main(claveString, textoEnClaroString):

    clave = []
    textoEnClaro = []

    clave = cadenaToMatrizBytes(claveString)
    textoEnClaro = cadenaToMatrizBytes(textoEnClaroString)

    aes(clave, textoEnClaro)

clave = input("Introduzca la clave: ")
textoEnClaro = input("Introduzca el texto en claro: ")

main(clave, textoEnClaro)