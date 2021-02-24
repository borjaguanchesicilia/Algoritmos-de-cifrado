# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.con
# Date: 23/02/2021
# File cifradoVigenere.py: Implementación del cifrado y descifrado de Vigenère.

import sys
import funciones as F

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

texto = input("Introduzca el texto: ")
texto = texto.replace(" ", "")
clave = input("Introduzca la clave: ")

textoNum = F.pasar_a_numero(abc, texto)
print("El texto con números es: ", textoNum)


claveNum = F.pasar_a_numero(abc, clave)
print("La clave con números es: ", claveNum)


cifradoNum = []
cont = 0
for i in range(len(texto)):
    if (cont+1 == len(clave)):
        cifradoNum.append((claveNum[cont] + textoNum[i]) % 26)
        cont = 0
    else:
        cifradoNum.append((claveNum[cont] + textoNum[i]) % 26)
        cont += 1

print("El texto cifrado con números es: ", cifradoNum)


cifrado = F.pasar_a_letras(abc, cifradoNum)
print("El texto cifrado es: ", cifrado)


resp = input("¿Quiere descifrar el mensaje? S/n  ")

if resp == 'S' or resp == 's':

    textoCifradoNum = []
    for i in range(len(cifrado)):
        for j in range(len(abc)):
            if (cifrado[i] == abc[j]):
                textoCifradoNum.append(j)

    print("El texto cifrafo con números es: ", textoCifradoNum)


    desCifradoNum = []
    cont = num = 0
    for i in range(len(textoCifradoNum)):
        if (cont+1 == len(clave)):
            num = (textoCifradoNum[i] - claveNum[cont]) % 26
            if num < 0:
                num = num + 26
                
            desCifradoNum.append(num)
            cont = 0
        else:
            num = (textoCifradoNum[i] - claveNum[cont]) % 26
            if num < 0:
                num = num + 26
                
            desCifradoNum.append(num)
            cont += 1
    
    print("El texto descifrafo con números es: ", desCifradoNum)


    desCifrado = F.pasar_a_letras(abc, desCifradoNum)
    print("El texto descifrado es: ", desCifrado)

else:
    print("Saliendo del programa...")
    sys.exit()