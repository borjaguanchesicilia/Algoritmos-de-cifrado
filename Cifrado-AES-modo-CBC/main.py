# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 19/04/2021
# File main.py Recogida del texto en claro, de la clave y del vector de inicialización


from modoCbc import *
from aes import *


def main(claveString, textoEnClaroString, vectorInicializacionString):

    clave = []
    textoEnClaro = []

    clave = cadenaToMatrizBytes(claveString)
    textoEnClaro = cadenaToMatrizBytes(textoEnClaroString)
    vectorInicializacion = cadenaToMatrizBytes(vectorInicializacionString)

    cbc(clave, textoEnClaro, vectorInicializacion)

clave = input("Introduzca la clave: ")
textoEnClaro = input("Introduzca el texto en claro: ")
vectorInicializacion = input("Introduzca el vector de inicialización (IV): ")

main(clave, textoEnClaro, vectorInicializacion)