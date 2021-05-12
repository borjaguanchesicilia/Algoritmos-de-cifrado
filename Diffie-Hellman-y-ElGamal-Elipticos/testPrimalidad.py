# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 12/05/2021
# File testPrimalidad.py: Implementación del test de primalidad de Lehman y Peralta.


import random
from exponenciacionRapida import *


def primos(p, ficheroExpoRapida):

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
        num = exponenciacionRapida(i,(p-1)/2, p, ficheroExpoRapida)
        if num != 1:
            if num == -1:
                flagNoPrimo = 1
                break

    if flagNoPrimo == 1:
        print(p, " es compuesto")
        return False
    else:
        return True