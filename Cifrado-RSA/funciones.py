# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 03/05/2021
# File funciones.py: Implementación de funciones auxiliares para el cifrado RSA.


import sys
import random
from math import *
from exponenciacionRapida import * 


def primos(p, f):

    primosPequenos = [2, 3, 5, 7, 11]
    flagNoPrimo = 0

    for i in primosPequenos:
        if p % i == 0 and p != i:
            print(f'{p} es divisible entre {i}, luego no es primo.')
            return False

    enterosAleatorios = []
    for i in range(6):
        num = random.randint(2, p-1)
        while num in enterosAleatorios:
            num = random.randint(1, p-1)
        enterosAleatorios.append(num)

    for i in enterosAleatorios:
        num = exponenciacionRapida(i,(p-1)/2, p, f)
        if num != 1:
            if num == -1:
                flagNoPrimo = 1
                break

    if flagNoPrimo == 1:
        print(p, " es compuesto")
        return False
    else:
        return True


def codificacionMensaje(textoEnClaro, n):

    textoEnClaro = textoEnClaro.replace(" ", "")
    l = []

    tamBloque = floor(log(n) / log(26))

    for i in range(0, len(textoEnClaro), tamBloque):
        lAux = []
        aux = i
        while aux != i + tamBloque:
            lAux.append(textoEnClaro[aux])
            aux = aux + 1
        l.append(lAux)

    bloquesCodificados = []

    for i in l:
        bloquesCodificados.append(codificarBloques(i, tamBloque))

    return tamBloque, bloquesCodificados


def codificarBloques(bloque, tamBloque):

    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    sumBloques = 0

    for i in range(0, len(bloque), 1):
        pos = abc.index(bloque[i])
        expo = pos*(26**(tamBloque-1-i))
        sumBloques = sumBloques + expo

    return sumBloques


def cifrado(bloques, e, n, f):

    result = []

    for i in bloques:
        result.append(exponenciacionRapida(i, e, n, f))

    return result