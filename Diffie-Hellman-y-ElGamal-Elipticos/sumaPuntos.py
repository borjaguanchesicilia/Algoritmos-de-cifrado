from euclidesExtendido import *
from fractions import *


def sumaPuntosIguales(p, a, P, ficheroEuclidesExten):  # p --> primo, a --> parámetro de la curva, P --> punto
    
    num = 3*(P[0]**2)+a
    den = 2*P[1]

    if ((num % den) != 0):
        l = (euclides(Fraction(num, den).denominator, p, ficheroEuclidesExten)*Fraction(num, den).numerator) % p
    else:
        l = (num / den) % p

    x3 = int((l**2 - P[0] - P[0]) % p)

    y3 = int((l*(P[0]-x3)-P[1]) % p)

    return [x3, y3]


def sumaPuntosDistintos(p, P, Q, ficheroEuclidesExten): # p --> primo, P y Q --> puntos distintos
    
    num = Q[1] - P[1]
    den = Q[0] - P[0]

    if ((num % den) != 0):
        l = (euclides(Fraction(num, den).denominator, p, ficheroEuclidesExten)*Fraction(num, den).numerator) % p
    else:
        l = (num / den) % p

    x3 = int((l**2 - P[0] - Q[0]) % p)

    y3 = int((l * (P[0] - x3) - P[1]) % p)

    return [x3, y3]