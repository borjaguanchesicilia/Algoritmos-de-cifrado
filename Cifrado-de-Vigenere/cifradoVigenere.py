# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.con
# Date: 23/02/2021
# File cifradoVigenere.py: Implementación del cifrado y descifrado de Vigenère.

import funciones as F

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

resp = input("¿Quiere cifrar un mensaje? S/n  ")

if resp == 'S' or resp == 's':

    texto = input("Introduzca el texto: ")
    texto = texto.replace(" ", "")
    clave = input("Introduzca la clave: ")

    textoNum = F.pasar_a_numero(abc, texto)
    claveNum = F.pasar_a_numero(abc, clave)

    cifradoNum = []
    cont = 0
    for i in range(len(texto)):
        cifradoNum.append((claveNum[cont] + textoNum[i]) % 26)
        if (cont+1 == len(clave)):
            cont = 0
        else:
            cont += 1

    cifrado = F.pasar_a_letras(abc, cifradoNum)
    print("El texto cifrado es: ", cifrado)

elif resp == 'N' or resp == 'n':

    resp = input("¿Quiere descifrar un mensaje? S/n  ")

    if resp == 'S' or resp == 's':

        texto = input("Introduzca el texto cifrado: ")
        clave = input("Introduzca la clave: ")

        textoNum = F.pasar_a_numero(abc, texto)
        claveNum = F.pasar_a_numero(abc, clave)

        desCifradoNum = []
        cont = num = 0
        for i in range(len(textoNum)):
            num = (textoNum[i] - claveNum[cont]) % 26
            if num < 0:
                num = num + 26         
            desCifradoNum.append(num)
            if (cont+1 == len(clave)):
                cont = 0
            else:
                cont += 1

        desCifrado = F.pasar_a_letras(abc, desCifradoNum)
        print("El texto descifrado es: ", desCifrado)

    else:
        F.error()
else:
    F.error()