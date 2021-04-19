# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 19/04/2021
# File modoCbc.py: Implementación del modo CBC para el cifrado AES.


from aes import *
import sys


# Función que realiza el modo CBC para AES
def cbc(clave, textoEnClaro, vectorInicializacion):

    contador = 0; flagInicio = 1
    aux = []; textoCifrado = []; textoCifradoCipherStealing = []; resultadoTextoCifrado = []

    # Comprobamos si la longitud del texto en claro es múltiplo de la longitud del bloque (16). Si es múltiplo
    # se aplica el modo CBC, en caso negativo, se aplica el modo CBC con Cipher Stealing.
    if len(textoEnClaro) % 16 != 0:
        print("\nLa longitud del texto en claro (%d) no es múltipo de la longitud de bloque." %(len(textoEnClaro)%16))
        print("Aplicando el nodo Cipher Stealing...")
        cipherStealing(clave, textoEnClaro, vectorInicializacion ,len(textoEnClaro) % 16)

    else:
        for i in range(len(textoEnClaro)):
            if (i == len(textoEnClaro)-1):
                i = i - 1
                while(len(aux) != 16):
                    aux.append(textoEnClaro[i])
                    i = i + 1
                textoCifrado = aes(clave, operacionXorBytes(aux, textoCifrado))
                resultadoTextoCifrado.append(textoCifrado)
                break

            if contador <16:
                if flagInicio == 1:
                    aux.append(textoEnClaro[i])
                    
                else:
                    aux.append(textoEnClaro[i-1])

                contador = contador + 1
            else:
                if flagInicio == 1:
                    textoCifrado = aes(clave, operacionXorBytes(aux, vectorInicializacion)) # Caso inicial
                    resultadoTextoCifrado.append(textoCifrado)
                    flagInicio = 0
                else:
                    textoCifrado = aes(clave, operacionXorBytes(aux, textoCifrado))
                    resultadoTextoCifrado.append(textoCifrado)

                contador = 0
                aux = []

        print("\n\nResultados:\n")
        for i in range(len(resultadoTextoCifrado)):
            print("Bloque %d de Texto Cifrado:" %(i+1), matrizToString(resultadoTextoCifrado[i]))


# Función que realiza el Cipher Stealing para CBC
def cipherStealing(clave, textoEnClaro, vectorInicializacion ,tam):

    contador = 0; flagInicio = 1; flagUltimo = 0
    aux = []; textoCifrado = []; textoCifradoCipherStealing = []; resultadoTextoCifrado = []


    for i in range(len(textoEnClaro)):
        if flagUltimo == 1 and i == len(textoEnClaro)-1:
            aux.append(textoEnClaro[i])
            while(len(aux) != 16):
                aux.append("00")
            textoCifrado = aes(clave, operacionXorBytes(aux, textoCifradoCipherStealing))
            break
        elif (i == len(textoEnClaro)-tam):
            flagUltimo = 1
            if flagInicio == 1:
                textoCifradoCipherStealing = aes(clave, operacionXorBytes(aux, vectorInicializacion))
                flagInicio = 0
                
            else:
                while(len(aux) != 16):
                    aux.append(textoEnClaro[i-1])
                    i = i + 1
                textoCifradoCipherStealing = aes(clave, operacionXorBytes(aux, textoCifrado))
            
            contador = 0
            aux=[]
            

        if contador < 16:
            aux.append(textoEnClaro[i])
            contador = contador + 1
        else:
            if flagInicio == 1:
                textoCifrado = aes(clave, operacionXorBytes(aux, vectorInicializacion))
                resultadoTextoCifrado.append(textoCifrado)
                flagInicio = 0
            else:
                textoCifrado = aes(clave, operacionXorBytes(aux, textoCifrado))
                resultadoTextoCifrado.append(textoCifrado)

            contador = 0
            aux = []


    resultadoTextoCifrado.append(textoCifrado)
    resultadoTextoCifrado.append(textoCifradoCipherStealing[:tam])

    print("\n\nResultados:\n")
    for i in range(len(resultadoTextoCifrado)):
        print("Bloque %d de Texto Cifrado:" %(i+1), matrizToString(resultadoTextoCifrado[i]))


# Función que realiza la xor antes de invocar al cifrado AES
def operacionXorBytes(texto1, texto2):
    
    resultado = []

    for i in range(len(texto1)):
        aux = hex(int(texto1[i], 16) ^ int(texto2[i], 16))[2:]
        if len(aux) < 2:
            aux = "0" + aux
            
        resultado.append(aux)

    print("\n\nResultado XOR CBC", resultado, "\n")

    return resultado