# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 26/04/2021
# File elGamal.py: Implementación del algoritmo de cifrado ElGamal.


from exponenciacionRapida import *
from euclidesExtendido import *


def elGamal(p, a, k, x, m):

    f=open("exponenciacionRapida.txt", "w")
    g=open("euclidesExtendido.txt", "w")

    print("Entrada: p = %d" %p, ", a = %d" %a, ", k = %d" %k, ", x = %d" %x, ", m = %d" %m)

    # Calculamos valor público de Alice:

    yA = exponenciacionRapida(a, k, p, f)

    # Calculamos valor público de Bob:

    yB = exponenciacionRapida(a, x, p, f)


    # Calculo de la clave compartida entre Alice y Bob (va a ser la misma):

    kA = exponenciacionRapida(yB, k, p, f)

    kB = exponenciacionRapida(yA, x, p, f)


    # Ciframos el mensaje:

    C = (kA * m) % p


    # Calculo de la inversa de la clave compartida:

    kInversa = euclidesExtendido(kB, p, g)


    # Desciframos el mensaje:

    M = (kInversa * C) % p


    print("Salida: yA = %d" %yA, ", yB = %d" %yB, ", K = %d" %kA, ", C = %d" %C, ", K-1 = %d" %kInversa, ", M = %d" %M)