from math import *
from euclidesExtendido import *
from copy import *
from fractions import *

def calculosPuntosX(p, a, b):

    puntos = []

    for i in range(p):
        aux = (i**3+a*i+b) % p
        puntos.append([i, aux])

    return puntos


def calculosPuntosY(p):
    
    puntos = []

    for i in range(p):
        aux = (i**2) % p
        puntos.append([aux, i])

    return puntos


def codificarMensaje(p, m, puntosValidos):

    if (m == 0):
        M = 2**(int(log(1) / log(2))+1)
    else:
        M = 2**(int(log(m) / log(2))+1)

    print(f'M = {M}')

    h = floor(p/M)
    print(f'h = {h} < {p} / {M}')
    
    j = 0
    mensajeCodificado = []
    while (True):
        aux = m * h + j
        for i in range(len(puntosValidos)):
            if (aux == puntosValidos[i][0]):
                mensajeCodificado = puntosValidos[i]
                print(f'El mensaje original codificado como punto Qm = ({m}*{h}+{i}, {mensajeCodificado[1]}) = ({mensajeCodificado[0]}, {mensajeCodificado[1]})')
                break
        if (mensajeCodificado != []):
            break
        j = j + 1

    return mensajeCodificado


def potencias2(n):

    result = []
    total = []

    binary = bin(n)[:1:-1]

    for x in range(len(binary)):
        if int(binary[x]):
            result.append(2**x)

    for i in range(len(result)):
        if (result[i] != 1 and result[i] != 2):
            aux = result[i]
            lista = []
            while aux != 2:
                aux = aux /2
                lista.append(2)
            lista.append(2)
            total.append(lista)
        else:
            total.append(result[i])

    return total


def puntoPorPotencias(lista, p, a, P, f):
    
    puntoAux = P
    for i in range(len(lista)):
        puntoAux = sumaPuntosIguales(p, a, puntoAux, f)
    
    return puntoAux
    
    
def sumaPuntos(a, n, P, p, f):
    
    potencias = potencias2(n)
    flagActivo = 0
    puntoAux = P
    
    if len(potencias) == 1: # Si es 2 --> [2], 4 --> [2, 2], 8 --> [2, 2, 2], 16 --> [2, 2, 2, 2]...
        if potencias == [2]:
            puntoAux = sumaPuntosIguales(p, a, puntoAux, f) # Caso [2] 2P
        else:
            puntoAux = puntoPorPotencias(potencias[0], p, a, P, f) # Resto de potencias de 2 --> 2^n P
    else: # Si es del tipo [1, 2], [2, [2, 2]]...
        puntoAux = P
        for i in range(len(potencias)):
            if type(potencias[i]) is list: # Es una lista de potencias: [2, 2, 2]... 2^n P
                puntoAux = puntoPorPotencias(potencias[i], p, a, puntoAux, f)
            elif potencias[i] == 1: # Es un 1 --> [1, 2] P
                flagActivo = 1
            elif potencias[i] == 2: # Es un 2 pero sin estar en una lista --> 2P
                puntoAux = sumaPuntosIguales(p, a, puntoAux, f)

    if flagActivo == 1: # Caso en que hay un 1: [1, 2] --> 3P, [1, [2, 2]] --> 5P
        puntoAux = sumaPuntosDistintos(p, P, puntoAux, f)
        
    return puntoAux


def sumaPuntosIguales(p, a, P, f):
    
    num = 3*(P[0]**2)+a
    den = 2*P[1]

    if ((num % den) != 0):
        l = (euclides(Fraction(num, den).denominator, p, f)*Fraction(num, den).numerator) % p
    else:
        l = (num / den) % p

    x3 = int((l**2 - P[0] - P[0]) % p)

    y3 = int((l*(P[0]-x3)-P[1]) % p)

    return [x3, y3]


def sumaPuntosDistintos(p, P, Q, f):
    
    num = Q[1] - P[1]
    den = Q[0] - P[0]

    if ((num % den) != 0):
        l = (euclides(Fraction(num, den).denominator, p, f)*Fraction(num, den).numerator) % p
    else:
        l = (num / den) % p

    x3 = int((l**2 - P[0] - Q[0]) % p)

    y3 = int((l * (P[0] - x3) - P[1]) % p)

    return [x3, y3]