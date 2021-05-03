# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 03/05/2021
# File main.py: FUnción principal.


from rsa import * 


def main():
    textoEnClaro = input("Introduzca el mensaje a cifrar: ")
    p = int(input("Introduzca el parámetro p: "))
    q = int(input("Introduzca el parámetro q: "))
    d = int(input("Introduzca el parámetro d: "))

    rsa(textoEnClaro, p, q, d)

main()