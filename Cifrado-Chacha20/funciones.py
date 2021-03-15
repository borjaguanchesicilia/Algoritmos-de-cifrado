import sys


# Función para recoger la clave, el contador y el nonce del fichero de entrada
def leerFichero(fichero):
    clave = []
    contador = []
    nonce = []
    resultado = []
    f = open(fichero)
    linea = f.readline()
    if (linea == "Clave:\n"):
        for i in range(8):
            linea = f.readline()
            clave.append(linea.strip("\n"))
    else:
        sys.exit()

    linea = f.readline()
    if (linea == "Contador:\n"):
        linea = f.readline()
        contador.append(linea.strip("\n"))
    else:
        sys.exit()

    linea = f.readline()
    if (linea == "Nonce:\n"):
        for i in range(3):
            linea = f.readline()
            nonce.append(linea.strip("\n"))
    else:
        sys.exit()
                 
    resultado.append(clave)
    resultado.append(contador)
    resultado.append(nonce)
    return resultado


# Función para convertir una string en un hexadecimal en formato little endian
def toLittleEndian(str):
    littleEndian = ""
    for i in range(len(str)):
        if str[i] == ':':
            littleEndian = str[i-1] + littleEndian
            littleEndian = str[i-2] + littleEndian

    littleEndian = str[10] + littleEndian
    littleEndian = str[9] + littleEndian
    littleEndian = "0x" + littleEndian

    return hex(int(littleEndian, 16))


# Función para mostrar el estado 
def mostrarEstado(x):
    print(x[0][2:], x[1][2:], x[2][2:], x[3][2:])
    print(x[4][2:], x[5][2:], x[6][2:], x[7][2:])
    print(x[8][2:], x[9][2:], x[10][2:], x[11][2:])
    print(x[12][2:], x[13][2:], x[14][2:], x[15][2:], "\n\n")