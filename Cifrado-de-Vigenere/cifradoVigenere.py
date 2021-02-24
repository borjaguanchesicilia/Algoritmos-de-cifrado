# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.con
# Date: 23/02/2021
# File cifradoVigenere.py: Implementación del cifrado y descifrado de Vigenère.

import funciones as F

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

res = input("¿Quiere cifrar un mensaje? S/n  ")

if res == 'S' or res == 's':

    men = input("Introduzca el mensaje: ")
    men = men.replace(" ", "")
    clave = input("Introduzca la clave: ")

    menNum = F.pasar_a_numero(abc, men)
    claveNum = F.pasar_a_numero(abc, clave)

    cifradoNum = []
    cont = 0
    for i in range(len(men)):
        cifradoNum.append((claveNum[cont] + menNum[i]) % 26)
        if (cont+1 == len(clave)):
            cont = 0
        else:
            cont += 1

    cifrado = F.pasar_a_letras(abc, cifradoNum)
    print("El mensaje cifrado es: ", cifrado)

elif res == 'N' or res == 'n':

    res = input("¿Quiere descifrar un mensaje? S/n  ")

    if res == 'S' or res == 's':

        men = input("Introduzca el mensaje cifrado: ")
        clave = input("Introduzca la clave: ")

        menNum = F.pasar_a_numero(abc, men)
        claveNum = F.pasar_a_numero(abc, clave)

        desCifradoNum = []
        cont = num = 0
        for i in range(len(menNum)):
            num = (menNum[i] - claveNum[cont]) % 26
            if num < 0:
                num = num + 26         
            desCifradoNum.append(num)
            if (cont+1 == len(clave)):
                cont = 0
            else:
                cont += 1

        desCifrado = F.pasar_a_letras(abc, desCifradoNum)
        print("El mensaje descifrado es: ", desCifrado)

    else:
        F.error()
else:
    F.error()