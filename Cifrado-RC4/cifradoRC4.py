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
