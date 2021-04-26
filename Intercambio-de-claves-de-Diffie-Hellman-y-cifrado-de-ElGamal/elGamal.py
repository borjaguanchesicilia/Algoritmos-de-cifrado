from exponenciacionRapida import *
from euclidesExtendido import *


def elGamal(p, a, k, x, m):

    print("Entrada: p = %d" %p, ", a = %d" %a, ", k = %d" %k, ", x = %d" %x, ", m = %d" %m)

    # Calculamos valor público de Alice:

    yA = exponenciacionRapida(a, k, p)

    # Calculamos valor público de Bob:

    yB = exponenciacionRapida(a, x, p)


    # Calculo de la clave compartida entre Alice y Bob:

    kA = exponenciacionRapida(yB, k, p)

    kB = exponenciacionRapida(yA, x, p)


    # Ciframos el mensaje:

    C = (kA * m) % p


    # Calculo de la inversa de la clave compartida:

    kInversa = euclidesExtendido(kB, p)


    # Desciframos el mensaje:

    M = (kInversa * kB * m) % p


    print("Salida: yA = %d" %yA, ", yB = %d" %yB, ", K = %d" %kA, ", C = %d" %C, ", K-1 = %d" %kInversa, ", M = %d" %M)