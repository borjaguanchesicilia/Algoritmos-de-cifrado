# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 30/03/2021
# File multiplicacion.py: Implementación de la multiplicación para el AES


# Función principal. Separamos los ceros, aplicamos la distributiva y operamos
def multiplicacion(byte1, byte2, byteAlgoritmo):
    
    # Separamos los 1's del byte2
    separacion1s = []
    k = 0
    aux = ""
    for i in range(len(byte2)):
        if byte2[i] == "1":
            if i != 0:
                while True:
                    aux = aux + "0"
                    k = k + 1
                    if (k == i):
                        break
            aux = aux + "1"
            while len(aux) < 8:
                aux = aux + "0"
            separacion1s.append(aux)
            k = 0
            aux = ""

    # Aplicamos la propiedad distributiva
    resultados = []

    for i in range(len(separacion1s)):
        if separacion1s[i][7] == "1": # 00000001
            resultados.append(byte1)
        else:
            resultados.append(desplazamientos(byte1, separacion1s[i], byteAlgoritmo))

    # Sumamos los bytes resultantes
    resultado = 0

    for i in range(len(resultados)):
        resultado = resultado ^ int(resultados[i], 2)

    return hex(resultado)


# Función para comprobar y realizar los desplazamientos  
def desplazamientos(byte1, byte2, byteAlgoritmo):
    
    desplazamiento = 0
    for i in range(len(byte2)):
        if byte2[i] == "1":
            desplazamiento = i
            break

    desplazamiento = 7 - desplazamiento

    valor = byte1
    iteracion = 0
    for i in range(desplazamiento):
        if valor[0] == "1": # Desplazamos y sumamos byte Snow3G | AES
            valor = valor[1:]
            valor = valor + "0"
            valor = int(valor, 2) ^ int(byteAlgoritmo, 2)
            valor = completar(str(bin(valor)[2:]))
        else: # Desplazamos
            valor = valor[1:]
            valor = valor + "0"
        iteracion = iteracion + 1

    return valor


# Función para pasar los bytes a binario
def bytesABinario(byte):

    valor = str(bin(byte)[2:])

    valor = completar(valor)

    return valor


# Función para completar con ceros los números en binario
def completar(valor):

    while len(valor) < 8:
        valor = "0" + valor

    return valor