def multiplicacion(byte1, byte2, algoritmo):
    
    separacionUnos = []
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
            separacionUnos.append(aux)
            k = 0
            aux = ""

    print(separacionUnos)



def separarBytes(byte):

    binario = ""
    aux = ""
    for i in range(len(byte)):
        if len(str(bin(int(byte[i]))[2:])) < 4:
            if len(str(bin(int(byte[i]))[2:])) == 1:
                binario = binario + "000" + str(bin(int(byte[i]))[2:])
            elif len(str(bin(int(byte[i]))[2:])) == 2:
                binario = binario + "00" + str(bin(int(byte[i]))[2:])
            elif len(str(bin(int(byte[i]))[2:])) == 3:
                binario = binario + "0" + str(bin(int(byte[i]))[2:])          
        else:
            binario = binario + str(bin(int(byte[i]))[2:])

    return binario




byte1 = input("Introduzca el byte 1: ")
byte2 = input("Introduzca el byte 2: ")


byte1 = separarBytes(byte1)
byte2 = separarBytes(byte2)
print("\n\nEl byte 1 sería: ", byte1)
print("El byte 2 sería: ", byte2)

print("\n\n¿Para qué algoritmo? Snow3G (0)  AES (1)")
multiplicacion(byte1, byte2, 1)