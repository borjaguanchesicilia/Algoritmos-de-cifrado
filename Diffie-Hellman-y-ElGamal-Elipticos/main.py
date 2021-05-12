from dhElgamalElipticos import * 
from testPrimalidad import * 

def main():

    ficheroExpoRapida = open("exponenciacionRapida.txt", "w")
    ficheroEuclidesExten = open("euclidesExtendido.txt", "w")

    p = 13
    a = 5
    b = 3
    G = [9, 6]
    da = 4
    db = 2
    m = 2

    if (primos(p, ficheroExpoRapida) == True): # Aplicamos el test de primalidad a p para saber si es primo
        if (4*(a**3)+27*(b**2) != 0): # 4a³+27b² != 0
            if (((G[1]**2)%p) == ((G[0]**3)+a*G[0]+b)%p): # Comprobamos si el punto pertenece a la curva
                elGamalEliptico(p, a, b, G, da, db, m, ficheroEuclidesExten)
            else:
                print(f'El punto base {G[0], G[1]} no pertenece a la curva.')
        else:
            print("No se cumple: 4a³+27b² != 0, cambie las constantes.")
    else:
        print("No es un primo suficientemente grande.")

main()