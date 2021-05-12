# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 26/04/2021
# File exponenciacionRapida.py: Implementación del algoritmo de exponenciación rápida.


def exponenciacionRapida(a, b, m, ficheroExpoRapida):
    
    x = 1
    y = a % m

    ficheroExpoRapida.write("\n\n %s ^"% str(a)+" %s" %str(b)+" (mod %s) \n" %str(m));
    ficheroExpoRapida.write("\ny:       b:       x:\n"); ficheroExpoRapida.write(str(y)+"      "+str(b)+"      "+str(x)+"\n")

    while (b > 0) and (y > 1):
        
        if (b % 2 != 0):

            x = (x * y) % m
            b = b - 1
            ficheroExpoRapida.write("         "+str(round(b))+"      "+str(x)+"\n")
        else:

            y = (y * y) % m
            b = b / 2
            ficheroExpoRapida.write(str(y)+"      "+str(round(b))+"\n")

    return (x)