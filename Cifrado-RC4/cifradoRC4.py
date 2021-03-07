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


def prga(S, texto):
    secCifr = []
    k = i = j = 0
    while(k < len(texto)):
        i = (i + 1) % 256
        j = (j+S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i]+S[j]) % 256
        secCifr.append(t)
        k += 1

    for i in range(len(secCifr)):
        secCifr[i] = S[secCifr[i]]
        secCifr[i] = str(bin(secCifr[i])[2:]) 

    return secCifr


def pasarBinario(texto):
    textoBinario = []
    for i in range(len(texto)):
        textoBinario.append(str(bin(texto[i])[2:]))

    return textoBinario


def cifrar(textoBinario, secuenciaCifrante):
    textoCifrado = []
    for i in range(len(textoBinario)):
        textoCifrado.append(bin(int(textoBinario[i], 2) ^ int(secuenciaCifrante[i], 2))[2:])

    return textoCifrado


def desCifrar(textoCifrado, secuenciaCifrante):
    textoDescifrado = []
    for i in range(len(textoCifrado)):
        textoDescifrado.append(int(textoCifrado[i], 2) ^ int(secuenciaCifrante[i], 2))

    return textoDescifrado


def error():
    print("Saliendo del programa...")
    sys.exit()


res = input("¿Quiere cifrar el mensaje? S/n  ")

if res == 'S' or res == 's':
    semilla = [2, 5]
    texto = [1, 34]
    S = ksa(semilla)
    generacion = prga(S, texto)
    textoBinario = pasarBinario(texto)
    print("\nEl texto es: ", texto)
    print("\nLa semilla es: ", semilla)
    print("\nEl texto cifrado es: ", cifrar(textoBinario, generacion))
elif res == 'N' or res == 'n':
    semilla = ['10010000', '1110']
    textoCifrado = ['10010001', '101100']
    print("\nEl texto cifrado es: ", textoCifrado)
    print("\nLa semilla es: ", semilla)
    print("\nEl texto descifrado es: ", desCifrar(textoCifrado, semilla))
else:
    error()
