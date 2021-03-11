# Author: Borja Guanche Sicilia
# Mail: alu0101205908@ull.edu.es
# # Date: 01/03/2021
# File cifradoRC4.py: Implementación del cifrado y descifrado del algoritmo RC4.


def ksa(semilla, f):
    S = []
    K = []
    j = 0
    for i in range(256):
        S.append(i)
        K.append(semilla[i % len(semilla)])

    for i in range(256):
        j = ((j + S[i] + K[i]) % 256)
        S[i], S[j] = S[j], S[i]

    f.write("S = ")
    f.write(str(S))
    f.write("\n\nK = ")
    f.write(str(K))
    return S


def prga(S, textoEnClaro, f):
    bytesSecuenciaCifrante = []
    k = i = j = 0
    while(k < len(textoEnClaro)):
        i = (i + 1) % 256
        j = (j+S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i]+S[j]) % 256
        bytesSecuenciaCifrante.append(S[t])
        k += 1

    for i in range(len(bytesSecuenciaCifrante)):
        bytesSecuenciaCifrante[i] = str(bin(bytesSecuenciaCifrante[i])[2:])

    f.write("\n\nBytes secuencia cifrante = ")
    f.write(str(bytesSecuenciaCifrante))

    return bytesSecuenciaCifrante


def pasarABinario(textoEnClaro, f):
    textoEnBinario = []
    for i in range(len(textoEnClaro)):
        textoEnBinario.append(str(bin(textoEnClaro[i])[2:]))

    f.write("\n\nTexto en binario = ")
    f.write(str(textoEnBinario))

    return textoEnBinario


def cifrar(textoEnBinario, secuenciaCifrante, f):
    textoCifrado = []
    for i in range(len(textoEnBinario)):
        textoCifrado.append(bin(int(textoEnBinario[i], 2) ^ int(secuenciaCifrante[i], 2))[2:])

    f.write("\n\nTexto cifrado = ")
    f.write(str(textoCifrado))

    return textoCifrado


def desCifrar(textoCifrado, secuenciaCifrante):
    textoEnClaro = []
    for i in range(len(textoCifrado)):
        textoEnClaro.append(int(textoCifrado[i], 2) ^ int(secuenciaCifrante[i], 2))

    return textoEnClaro


def error():
    print("Saliendo del programa...")
    sys.exit()


res = input("¿Quiere cifrar el mensaje? S/n  ")

if res == 'S' or res == 's':
    f = open("cifrado.txt", "w")
    semilla = [2, 5]
    textoEnClaro = [1, 34]
    S = ksa(semilla, f)
    secuenciaCifrante = prga(S, textoEnClaro, f)
    textoEnBinario = pasarABinario(textoEnClaro, f)
    print("\nEl texto en claro es: ", textoEnClaro)
    print("\nLa semilla es: ", semilla)
    print("\nLa secuencia cifrante es: ", secuenciaCifrante)
    print("\nEl texto cifrado es: ", cifrar(textoEnBinario, secuenciaCifrante, f))
    f.close()
elif res == 'N' or res == 'n':
    secuenciaCifrante = ['10010000', '1110']
    textoCifrado = ['10010001', '101100']
    print("\nEl texto cifrado es: ", textoCifrado)
    print("\nLa secuencia cifrante es: ", secuenciaCifrante)
    print("\nEl texto descifrado es: ", desCifrar(textoCifrado, secuenciaCifrante))
else:
    error()
