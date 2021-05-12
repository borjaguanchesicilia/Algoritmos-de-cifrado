# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 26/04/2021
# File euclidesExtendido.py: Implementación del algoritmo de Euclides extendido.


def euclides(a, b, ficheroEuclidesExten):
    
    if b == 0:
        return 1
 
    z0 = 1; z1 = 0; zAux0 = 0; zAux1 = 1; i = 0

    ficheroEuclidesExten.write("\n\n %s"% str(a)+"^-1 "+" (mod %s) \n" %str(b))
    ficheroEuclidesExten.write("\ni        xi              zi")
    ficheroEuclidesExten.write("\n"+str(i)+ "      "+  "               "+str(zAux0))
    i = i + 1
    ficheroEuclidesExten.write("\n"+str(i)+ "      "+str(b)+  "               "+str(zAux1))
 
    while b != 0:
        cociente, resto = a//b, a%b
        z, zAux = z0 - cociente * z1, zAux0 - cociente * zAux1
        a = b; b = resto
        
        z0 = z1; z1 = z
        zAux0 = zAux1; zAux1 = zAux
        i = i + 1
        ficheroEuclidesExten.write("\n"+str(i)+ "      "+str(b)+  "               "+str(zAux1))
 
    ficheroEuclidesExten.write("\nResultado: "+str(z0))
    return  z0