# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.con
# Date: 23/02/2021
# File cifradoVigenere: Implementación del cifrado de Vigenère.

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