from elGamal import *

def main ():

    p = int(input("Introduzca el número primo compartido: "))
    a = int(input("Introduzca la raíz primitiva compartida: "))
    k = int(input("Introduzca el valor privado de Alice (persona que cifra): "))
    x = int(input("Introduzca la valor privado de Bob: "))
    m = int(input("Introduzca el mensaje a cifrar: "))

    elGamal(p, a, k, x, m)

main()