from funciones import * 
from euclidesExtendido import * 

def rsa(textoEnClaro, p, q, d):

    f=open("exponenciacionRapida.txt", "w")
    g=open("euclidesExtendido.txt", "w")

    if (primos(p, f)):
        if (primos(q, f)):
            print(f'{p} y {q} pueden ser primos')
            n = p*q
            print("INFORMACIÓN PÚBLICA: el valor de n es: ", n)
            phi = (p-1) * (q-1)
            print("El valor de phi es: ", phi)
            e = euclidesExtendido(d, phi, g)
            print("INFORMACIÓN PÚBLICA: El valor de e es: ", e)
            tamBloque, bloquesCodificados = codificacionMensaje(textoEnClaro, n)
            print("El tamaño del bloque es: ", tamBloque, " y los bloques son: ", bloquesCodificados)
            bloquesCifrados = cifrado(bloquesCodificados, e, n, f)
            print("Los bloques cifrados son: ", bloquesCifrados)
