def generador(estado1, estado2):
    primerRDLR, auxRDLR, realimentacion1, primerEstado, segundoRDLR, realimentacion2, segundoEstado, paraXor, secuencia = ([] for i in range(9))
    
    for i in range(10):
        primerRDLR.append(int(estado1[i]))
        segundoRDLR.append(int(estado2[i]))

    print("LFSR1                           realimentación    LFSR2                           realimentación     Secuencia C/A PRN1")

    for i in range(14):
        primerEstado = primerRDLR
        segundoEstado = segundoRDLR

        # LFSR1
        xor1 = primerRDLR[2] ^ primerRDLR[9]
        realimentacion1.append(xor1); auxRDLR.append(xor1)
        for j in range(10):
            auxRDLR.append(primerRDLR[j])
        paraXor.append(auxRDLR[10])
        auxRDLR.pop()
        primerRDLR.clear()
        for j in range(10):
            primerRDLR.append(auxRDLR[j])
        auxRDLR.clear()


        # LFSR2
        xor2 = segundoRDLR[1] ^ segundoRDLR[2] ^ segundoRDLR[5] ^ segundoRDLR[7] ^ segundoRDLR[8] ^ segundoRDLR[9]
        realimentacion2.append(xor2); auxRDLR.append(xor2)
        for j in range(10):
            auxRDLR.append(segundoRDLR[j])
        paraXor.append(auxRDLR[2])
        paraXor.append(auxRDLR[6])
        auxRDLR.pop()
        segundoRDLR.clear()
        for j in range(10):
            segundoRDLR.append(auxRDLR[j])
        auxRDLR.clear()
        
        secuencia.append(paraXor[0] ^ paraXor[1] ^ paraXor[2])
        paraXor.clear()

        #Mostrado
        print(primerEstado, "      ",xor1,"         ", segundoEstado, "      ",xor2,"                   ", secuencia[i])


    print("\n\nRealimentación 1:  ", realimentacion1, "\n")
    print("Realimentación 2:  ", realimentacion2, "\n")
    print("Secuencia C/A:  ", secuencia, "\n")

generador("1111111111","1111111111")