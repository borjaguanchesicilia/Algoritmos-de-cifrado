# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 12/05/2021
# File main.py: Función principal.


from dhElgamalElipticos import * 
from testPrimalidad import * 


def main():

    ficheroExpoRapida = open("exponenciacionRapida.txt", "w")
    ficheroEuclidesExten = open("euclidesExtendido.txt", "w")

    p = int(input("Introduzca el número primo: "))
    a = int(input("Introduzca la cte a de la curva: "))
    b = int(input("Introduzca la cte b de la curva: "))
    p0 = int(input("Introduzca la primera coordenada del punto base: "))
    p1 = int(input("Introduzca la segunda coordenada del punto base: "))
    da = int(input("Introduzca el secreto de Alice: "))
    db = int(input("Introduzca el secreto de Bob: "))
    m = int(input("Introduzca el mensaje a cifrar: "))

    if (primos(p, ficheroExpoRapida) == True): # Aplicamos el test de primalidad a p para saber si es primo
        if (4*(a**3)+27*(b**2) != 0): # 4a³+27b² != 0
            if (((p1**2)%p) == ((p0**3)+a*p0+b)%p): # Comprobamos si el punto pertenece a la curva
                elGamalEliptico(p, a, b, [p0, p1], da, db, m, ficheroEuclidesExten)
            else:
                print(f'El punto base {G[0], G[1]} no pertenece a la curva.')
        else:
            print("No se cumple: 4a³+27b² != 0, cambie las constantes.")
    else:
        print("No es un primo suficientemente grande.")

main()