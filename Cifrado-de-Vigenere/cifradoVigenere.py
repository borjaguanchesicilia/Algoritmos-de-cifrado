# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.con
# Date: 23/02/2021
# File cifradoVigenere: Implementación del cifrado de Vigenère.

import sys

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

texto = input("Introduzca el texto: ")
texto = texto.replace(" ", "")
clave = input("Introduzca la clave: ")

textoNum = []
for i in range(len(texto)):
    for j in range(len(abc)):
        if (texto[i] == abc[j]):
            textoNum.append(j)

print("El texto con números es: ", textoNum)


claveNum = []
tam = len(clave)
for i in range(tam):
    for j in range(len(abc)):
        if (clave[i] == abc[j]):
            claveNum.append(j)
    
print("La clave con números es: ", claveNum)

cifradoNum = []
cont = 0
for i in range(len(texto)):
    if (cont+1 == tam):
        cifradoNum.append((claveNum[cont] + textoNum[i]) % 26)
        cont = 0
    else:
        cifradoNum.append((claveNum[cont] + textoNum[i]) % 26)
        cont += 1

print("El texto cifrado con números es: ", cifradoNum)

cifrado = ""
for i in range(len(cifradoNum)):
    for j in range(len(abc)):
        if (cifradoNum[i] == j):
            cifrado = cifrado + abc[j]

print("El texto cifrado es: ", cifrado)

resp = input("¿Quiere descifrar el mensaje? S/n")

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
        if (cont+1 == tam):
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


    desCifrado = ""
    for i in range(len(desCifradoNum)):
        for j in range(len(abc)):
            if (desCifradoNum[i] == j):
                desCifrado = desCifrado + abc[j]

    print("El texto descifrado es: ", desCifrado)

else:
    print("Saliendo del programa...")
    sys.exit()