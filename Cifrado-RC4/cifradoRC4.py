# Author: Borja Guanche Sicilia
# Mail: alu0101205908@ull.edu.es
# # Date: 01/03/2021
# File cifradoRC4.py: Implementación del cifrado RC4.


def ksa(semilla):
    S = []
    K = []
    j = 0
    for i in range(256):
        S.append(i)
        K.append(semilla[i % len(semilla)])

    for i in range(256):
        j = ((j + S[i] + K[i]) % 256)
        S[i], S[j] = S[j], S[i]

    return S


def prga(S, textoEnClaro):
    bytesSecuenciaCifrante = []
    k = i = j = 0
    while(k < len(textoEnClaro)):
        i = (i + 1) % 256
        j = (j+S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i]+S[j]) % 256
        bytesSecuenciaCifrante.append(t)
        k += 1

    for i in range(len(bytesSecuenciaCifrante)):
        bytesSecuenciaCifrante[i] = S[bytesSecuenciaCifrante[i]]
        bytesSecuenciaCifrante[i] = str(bin(bytesSecuenciaCifrante[i])[2:]) 

    return bytesSecuenciaCifrante


def pasarABinario(textoEnClaro):
    textoEnBinario = []
    for i in range(len(textoEnClaro)):
        textoEnBinario.append(str(bin(textoEnClaro[i])[2:]))

    return textoEnBinario


def cifrar(textoEnBinario, secuenciaCifrante):
    textoCifrado = []
    for i in range(len(textoEnBinario)):
        textoCifrado.append(bin(int(textoEnBinario[i], 2) ^ int(secuenciaCifrante[i], 2))[2:])

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
    semilla = [2, 5]
    textoEnClaro = [1, 34]
    S = ksa(semilla)
    secuenciaCifrante = prga(S, textoEnClaro)
    textoEnBinario = pasarABinario(textoEnClaro)
    print("\nEl texto en claro es: ", textoEnClaro)
    print("\nLa semilla es: ", semilla)
    print("\nEl texto cifrado es: ", cifrar(textoEnBinario, secuenciaCifrante))
elif res == 'N' or res == 'n':
    secuenciaCifrante = ['10010000', '1110']
    textoCifrado = ['10010001', '101100']
    print("\nEl texto cifrado es: ", textoCifrado)
    print("\nLa secuencia cifrante es: ", secuenciaCifrante)
    print("\nEl texto descifrado es: ", desCifrar(textoCifrado, secuenciaCifrante))
else:
    error()
