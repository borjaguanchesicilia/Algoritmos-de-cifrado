from rsa import * 


def main():
    #textoEnClaro = input("Introduzca el mensaje a cifrar: ")
    #p = int(input("Introduzca el parámetro p: "))
    #q = int(input("Introduzca el parámetro q: "))
    #d = int(input("Introduzca el parámetro d: "))

    #textoEnClaro = "AMIGO MIO"
    #p = 2347
    #q = 347
    #d = 5

    textoEnClaro = "MANDA DINEROS"
    p = 421
    q = 7
    d = 1619

    rsa(textoEnClaro, p, q, d)

main()