# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 21/03/2021
# File ca.py: Implementación del generador C/A de GPS.


import copy
import sys

def generador(estado1, estado2):
    primerRDLR, auxRDLR, realimentacion1, primerEstado, estadoAnterior1, segundoRDLR, realimentacion2, segundoEstado, estadoAnterior2, xorFinal, secuencia = ([] for i in range(11))

    for i in range(10):
        primerRDLR.append(int(estado1[i]))
        segundoRDLR.append(int(estado2[i]))
        estadoAnterior1.append(int(estado1[i]))
        estadoAnterior2.append(int(estado2[i]))

    print("\n\nLFSR1                           realimentación    LFSR2                           realimentación     Secuencia C/A PRN1\n")

    for i in range(14):
        primerEstado = estadoAnterior1
        segundoEstado = estadoAnterior2

        # RDLR 1
        xor1 = primerRDLR[2] ^ primerRDLR[9]
        realimentacion1.append(xor1); auxRDLR.append(xor1)
        for j in range(10):
            auxRDLR.append(primerRDLR[j])
        xorFinal.append(auxRDLR[10])
        auxRDLR.pop()
        primerRDLR.clear()
        for j in range(10):
            primerRDLR.append(auxRDLR[j])
        auxRDLR.clear()


        # RDRL 2
        xor2 = segundoRDLR[1] ^ segundoRDLR[2] ^ segundoRDLR[5] ^ segundoRDLR[7] ^ segundoRDLR[8] ^ segundoRDLR[9]
        realimentacion2.append(xor2); auxRDLR.append(xor2)
        for j in range(10):
            auxRDLR.append(segundoRDLR[j])
        xorFinal.append(auxRDLR[2])
        xorFinal.append(auxRDLR[6])
        auxRDLR.pop()
        segundoRDLR.clear()
        for j in range(10):
            segundoRDLR.append(auxRDLR[j])
        auxRDLR.clear()
        
        secuencia.append(xorFinal[0] ^ xorFinal[1] ^ xorFinal[2])
        xorFinal.clear()


        #Mostrado
        print(primerEstado, "      ",xor1,"         ", segundoEstado, "      ",xor2,"                   ", secuencia[i])
        
        estadoAnterior1 = copy.deepcopy(primerRDLR)
        estadoAnterior2 = copy.deepcopy(segundoRDLR)

    print("\n\nRealimentación 1:  ", realimentacion1, "\n")
    print("Realimentación 2:  ", realimentacion2, "\n")
    print("Secuencia C/A:  ", secuencia, "\n")


def recogerDatos():
    estado1 = input("\n\nIntroduzca el estado del RDLR 1: ")
    estado2 = input("Introduzca el estado del RDLR 2: ")
    
    if ((len(estado1) != 10) or (len(estado2) != 10)):
        print("\nLos estados tienen que ser de 10 bits")
        print("\nSaliendo del programa...")
        sys.exit()
    else:
        generador(estado1, estado2)

recogerDatos()