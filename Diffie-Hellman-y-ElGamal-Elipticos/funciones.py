from math import *
from numpy import *
from matplotlib.pyplot import *
from sumaPuntos import *


def calculosPuntosX(p, a, b):

    puntos = []

    for i in range(p):
        aux = (i**3+a*i+b) % p # (x³+ax+b) mod p
        puntos.append([i, aux])

    return puntos


def calculosPuntosY(p):
    
    puntos = []

    for i in range(p):
        aux = (i**2) % p # y² mod p
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
        coordenadaX = m * h + j
        for i in range(len(puntosValidos)):
            if (coordenadaX == puntosValidos[i][0]):
                mensajeCodificado = puntosValidos[i]
                print(f'El mensaje original codificado como punto Qm = ({m}*{h}+{i}, {mensajeCodificado[1]}) = ({mensajeCodificado[0]}, {mensajeCodificado[1]})')
                break
        if (mensajeCodificado != []):
            break
        j = j + 1

    return mensajeCodificado


def potencias2(n):
    
    potencias = []; resultado = []

    binario = bin(n)[:1:-1]

    for i in range(len(binario)):
        if int(binario[i]) == 1:
            potencias.append(2**i)

    for i in range(len(potencias)):
        if (potencias[i] != 1 and potencias[i] != 2):
            valorAux = potencias[i]
            listaAux = []
            while valorAux != 2:
                valorAux = valorAux /2
                listaAux.append(2)
            listaAux.append(2)
            resultado.append(listaAux)
        else:
            resultado.append(potencias[i])

    return resultado


def puntoPorPotencias(lista, p, a, P, ficheroEuclidesExten):
    
    puntoAux = P
    for i in range(len(lista)):
        puntoAux = sumaPuntosIguales(p, a, puntoAux, ficheroEuclidesExten)
    
    return puntoAux
    
    
def sumaPuntos(a, n, P, p, ficheroEuclidesExten):
    
    potencias = potencias2(n)
    flagActivo = 0
    puntoAux = P
    
    if len(potencias) == 1 and potencias != [1]: # Si es 2 --> [2], 4 --> [2, 2], 8 --> [2, 2, 2], 16 --> [2, 2, 2, 2]...
        if potencias == [2]:
            puntoAux = sumaPuntosIguales(p, a, puntoAux, ficheroEuclidesExten) # Caso [2] 2P
        else:
            puntoAux = puntoPorPotencias(potencias[0], p, a, P, ficheroEuclidesExten) # Resto de potencias de 2 --> 2^n P
    else: # Si es del tipo [1, 2], [2, [2, 2]]...
        for i in range(len(potencias)):
            if type(potencias[i]) is list: # Es una lista de potencias: [2, 2, 2]... 2^n P
                puntoAux = puntoPorPotencias(potencias[i], p, a, puntoAux, ficheroEuclidesExten)
            elif potencias[i] == 1: # Es un 1 --> [1, 2] P
                flagActivo = 1
            elif potencias[i] == 2: # Es un 2 pero sin estar en una lista --> 2P
                puntoAux = sumaPuntosIguales(p, a, puntoAux, ficheroEuclidesExten)

    if flagActivo == 1: # Caso en que hay un 1: [1, 2] --> 3P, [1, [2, 2]] --> 5P
        if P != puntoAux:
            puntoAux = sumaPuntosDistintos(p, P, puntoAux, ficheroEuclidesExten)
        else:
            puntoAux = sumaPuntosIguales(p, a, puntoAux, ficheroEuclidesExten)
        
    return puntoAux


def graficarPuntos(puntosValidos, a, b):
    
    ejeX = []; ejeY = []

    for i in range(len(puntosValidos)):
        ejeX.append(puntosValidos[i][0])
        ejeY.append(puntosValidos[i][1])

    y, x = ogrid[-15:15:500j, -15:15:500j]
    contour(x.ravel(), y.ravel(), y**2 - x**3 - x*a-b, [0])
    plot(ejeX, ejeY, 'ro', color="red")
    grid()
    show()