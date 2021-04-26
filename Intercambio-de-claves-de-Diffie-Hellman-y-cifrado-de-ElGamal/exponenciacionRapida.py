# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 26/04/2021
# File exponenciacionRapida.py: Implementación del algoritmo de exponenciación rápida.


def exponenciacionRapida(a, b, m, f):

    x = 1
    y = a % m

    f.write("\n\n %s ^"% str(a)+" %s" %str(b)+" (mod %s) \n" %str(m));
    f.write("\ny:       b:       x:\n"); f.write(str(y)+"      "+str(b)+"      "+str(x)+"\n")

    while (b > 0) and (y > 1):
        
        if (b % 2 != 0):

            x = (x * y) % m
            b = b - 1
            f.write("         "+str(round(b))+"      "+str(x)+"\n")
        else:

            y = (y * y) % m
            b = b / 2
            f.write(str(y)+"      "+str(round(b))+"\n")

    return (x)