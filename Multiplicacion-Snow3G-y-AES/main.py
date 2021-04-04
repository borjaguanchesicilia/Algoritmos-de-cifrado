import sys
from multiplicacion import *


byte1 = int(input("Introduzca el byte 1 (EN HEXADECIMAL): "), 16)
byte2 = int(input("Introduzca el byte 2 (EN HEXADECIMAL): "), 16)

byte1 = bytesABinario(byte1)
byte2 = bytesABinario(byte2)

print("\n\nEl byte 1 sería: ", byte1)
print("El byte 2 sería: ", byte2)

algoritmo = int(input("\n\n¿Para qué algoritmo? Snow3G (0) | AES (1) "))

if algoritmo == 0:
    print("\nSe utilizará el byte A9 (10101001)")
    byteAlgoritmo = "10101001"
elif algoritmo == 1:
    print("\nSe utilizará el byte 1B (00011011)")
    byteAlgoritmo = "00011011"
else:
    print("El algoritmo tiene que ser Snow3G (0) | AES (1)")
    sys.exit()


multiplicacion(byte1, byte2, byteAlgoritmo)