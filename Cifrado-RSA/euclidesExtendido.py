# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 26/04/2021
# File euclidesExtendido.py: Implementación del algoritmo de Euclides extendido.


def euclidesExtendido(x, y, g):
   
    if x < y:
        return euclidesExtendido(y, x, g)

    a = x
    z = [0, 1]
    i = 0
    g.write("\n\n %s"% str(y)+"^-1 "+" (mod %s) \n" %str(x))
    g.write("\ni        xi              zi")
    g.write("\n"+str(i)+ "      "+  "               "+str(z[0]))
    i = i + 1
    g.write("\n"+str(i)+ "      "+str(x)+  "               "+str(z[1]))
    while y != 0:
        div = x // y
        x, y = y, x % y
        aux = ((div*(-1))*z[1]+z[0]) % a
        z.append(aux)
        z.pop(0)
        i = i + 1
        g.write("\n"+str(i)+ "      "+str(x)+  "               "+str(z[1]))

    return z[0]