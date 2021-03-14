def qr(a,b,c,d):

    a = int(a, 16)
    b = int(b, 16)
    c = int(c, 16)
    d = int(d, 16)

    a = (a + b)&0xffffffff
    d = d ^ a
    d = rotl(d, 16)

    c = (c + d)&0xffffffff
    b = b ^ c
    b = rotl(b, 12)

    a = (a + b)&0xffffffff
    d = d ^ a
    d = rotl(d, 8)

    c = (c + d)&0xffffffff
    b = b ^ c
    b = rotl(b, 7)

    return hex(a), hex(b), hex(c), hex(d)


def rotl(a, b):
    return ((a << b)&0xffffffff) | (a >> (32 - b))


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

    num = int(littleEndian, 16)
    return hex(num)


def inner_Block(x):

    x[0], x[4], x[8], x[12] = qr(x[0], x[4], x[8], x[12])
    x[1], x[5], x[9], x[13] = qr(x[1], x[5], x[9], x[13])
    x[2], x[6], x[10], x[14] = qr(x[2], x[6], x[10], x[14])
    x[3], x[7], x[11], x[15] = qr(x[3], x[7], x[11], x[15])

    x[0], x[5], x[10], x[15] = qr(x[0], x[5], x[10], x[15])
    x[1], x[6], x[11], x[12] = qr(x[1], x[6], x[11], x[12])
    x[2], x[7], x[8], x[13] = qr(x[2], x[7], x[8], x[13])
    x[3], x[4], x[9], x[14] = qr(x[3], x[4], x[9], x[14])

    return x


def chacha20Block(clave, contador, nonce):
    x = []
    entrada = []
    salida = []

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
    print(x[0][2:], x[1][2:], x[2][2:], x[3][2:])
    print(x[4][2:], x[5][2:], x[6][2:], x[7][2:])
    print(x[8][2:], x[9][2:], x[10][2:], x[11][2:])
    print(x[12][2:], x[13][2:], x[14][2:], x[15][2:], "\n\n")

    for i in range(10):
        inner_Block(x)
        

    print("Estado final tras las 20 iteraciones:\n")
    print(x[0][2:], x[1][2:], x[2][2:], x[3][2:])
    print(x[4][2:], x[5][2:], x[6][2:], x[7][2:])
    print(x[8][2:], x[9][2:], x[10][2:], x[11][2:])
    print(x[12][2:], x[13][2:], x[14][2:], x[15][2:], "\n\n")

    for i in range(16):
        salida.append(hex(int(x[i],16) + int(entrada[i],16)))

    print("Estado de salida del generador:\n")
    print(salida[0][2:], salida[1][2:], salida[2][2:], salida[3][2:])
    print(salida[4][2:], salida[5][2:], salida[6][2:], salida[7][2:])
    print(salida[8][2:], salida[9][2:], salida[10][2:], salida[11][2:])
    print(salida[12][2:], salida[13][2:], salida[14][2:], salida[15][2:])


clave = ['00:01:02:03', '04:05:06:07','08:09:0a:0b', '0c:0d:0e:0f', '10:11:12:13', '14:15:16:17', '18:19:1a:1b', '1c:1d:1e:1f']
contador = ['01:00:00:00']
nonce = ['00:00:00:09', '00:00:00:4a', '00:00:00:00']

chachaBlock(clave, contador, nonce)