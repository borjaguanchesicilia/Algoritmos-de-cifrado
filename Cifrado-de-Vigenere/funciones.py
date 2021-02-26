# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 23/02/2021
# File funciones.py: Funciones de ayuda a la implementación del cifrado de Vigenère.

import sys

def pasar_a_numero(abc, men):
    num = []
    for i in range(len(men)):
        for j in range(len(abc)):
            if (men[i] == abc[j]):
                num.append(j)
    return num

def pasar_a_letras(abc, num):
    str = ""
    for i in range(len(num)):
        for j in range(len(abc)):
            if (num[i] == j):
                str = str + abc[j]
    return str

def error():
    print("Saliendo del programa...")
    sys.exit()