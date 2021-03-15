# Author: Borja Guanche Sicilia
# Mail: alu0101205908@ull.edu.es
# # Date: 15/03/2021
# File chacha20.py: Implementación del cifrado Chacha20.


from funciones import *


# Función para relizar las operaciones de suma (en módulo 32), xor y desplazamiento
def qr(a,b,c,d):

    a = int(a, 16)
    b = int(b, 16)
    c = int(c, 16)
    d = int(d, 16)

    a = (a + b)&0xffffffff
    d = d ^ a
    d = rotacionAIzquierda(d, 16)

    c = (c + d)&0xffffffff
    b = b ^ c
    b = rotacionAIzquierda(b, 12)

    a = (a + b)&0xffffffff
    d = d ^ a
    d = rotacionAIzquierda(d, 8)

    c = (c + d)&0xffffffff
    b = b ^ c
    b = rotacionAIzquierda(b, 7)


    return hex(a), hex(b), hex(c), hex(d)


# Función para realizar el desplazamiento a izquierda de n bits
def rotacionAIzquierda(a, n):
    return ((a << n)&0xffffffff) | (a >> (32 - n))


# Función para realizar las operaciones qr en columnas y diagonales
def bloqueInterno(x):

    # Operaciones sobre columnas:

    x[0], x[4], x[8], x[12] = qr(x[0], x[4], x[8], x[12])
    x[1], x[5], x[9], x[13] = qr(x[1], x[5], x[9], x[13])
    x[2], x[6], x[10], x[14] = qr(x[2], x[6], x[10], x[14])
    x[3], x[7], x[11], x[15] = qr(x[3], x[7], x[11], x[15])

    # Operaciones sobre diagonales:

    x[0], x[5], x[10], x[15] = qr(x[0], x[5], x[10], x[15])
    x[1], x[6], x[11], x[12] = qr(x[1], x[6], x[11], x[12])
    x[2], x[7], x[8], x[13] = qr(x[2], x[7], x[8], x[13])
    x[3], x[4], x[9], x[14] = qr(x[3], x[4], x[9], x[14])

    return x


def BloqueChacha20(clave, contador, nonce):
    x = []
    entrada = []
    salida = []
    descifrado = []

    #Constantes (128 bits) 4 palabras
    x.append(hex(0x61707865))
    x.append(hex(0x3320646e))
    x.append(hex(0x79622d32))
    x.append(hex(0x6b206574))

    entrada.append(hex(0x61707865))
    entrada.append(hex(0x3320646e))
    entrada.append(hex(0x79622d32))
    entrada.append(hex(0x6b206574))

    #Clave (256 bits) 8 palabras en Little endian
    for i in range(len(clave)):
        x.append(toLittleEndian(clave[i]))
        entrada.append(toLittleEndian(clave[i]))

    #Contador (32 bits) 1 palabra en Little endian
    for i in range(len(contador)):
        x.append(toLittleEndian(contador[i]))
        entrada.append(toLittleEndian(contador[i]))

    #Nonce (96 bits) 3 palabras en Little endian
    for i in range(len(nonce)):
        x.append(toLittleEndian(nonce[i]))
        entrada.append(toLittleEndian(nonce[i]))

   
    print("Estado inicial:\n")
    mostrarEstado(x)

    for i in range(10):
        bloqueInterno(x)
        

    print("Estado final tras las 20 iteraciones:\n")
    mostrarEstado(x)


    for i in range(16):
        salida.append(hex(int(x[i],16) + int(entrada[i],16)&0xffffffff))

    print("Estado de salida del generador:\n")
    mostrarEstado(salida)


BloqueChacha20(leerFichero("entrada.txt")[0], leerFichero("entrada.txt")[1], leerFichero("entrada.txt")[2])