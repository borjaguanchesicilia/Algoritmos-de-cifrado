def principal(estado1, estado2):
    primerRDLR = []
    auxPrimerRDLR = []
    realimentacion1 = []
    segundoRDLR = []
    auxSegundoRDLR = []
    realimentacion2 = []
    primerEstado = []
    segundoEstado = []
    paraXor = []
    secuencia = []
    for i in range(10):
        primerRDLR.append(int(estado1[i]))
        segundoRDLR.append(int(estado2[i]))

    primerEstado = primerRDLR
    segundoEstado = segundoRDLR

    print("LFSR1                           realimentación    LFSR2                           realimentación     Secuencia C/A PRN1")

  
    for i in range(14):
        primerEstado = primerRDLR
        segundoEstado = segundoRDLR

        # LFSR1
        xor1 = primerRDLR[2] ^ primerRDLR[9]
        realimentacion1.append(xor1)
        auxPrimerRDLR.append(xor1)
        for j in range(10):
            auxPrimerRDLR.append(primerRDLR[j])
        paraXor.append(auxPrimerRDLR[10])
        auxPrimerRDLR.pop()
        primerRDLR = []
        for j in range(10):
            primerRDLR.append(auxPrimerRDLR[j])
        auxPrimerRDLR = []


        # LFSR2
        xor2 = segundoRDLR[1] ^ segundoRDLR[2] ^ segundoRDLR[5] ^ segundoRDLR[7] ^ segundoRDLR[8] ^ segundoRDLR[9]
        realimentacion2.append(xor2)
        auxSegundoRDLR.append(xor2)
        for j in range(10):
            auxSegundoRDLR.append(segundoRDLR[j])
        paraXor.append(auxSegundoRDLR[2])
        paraXor.append(auxSegundoRDLR[6])
        auxSegundoRDLR.pop()
        segundoRDLR = []
        for j in range(10):
            segundoRDLR.append(auxSegundoRDLR[j])
        auxSegundoRDLR = []
        
        secuencia.append(paraXor[0] ^ paraXor[1] ^ paraXor[2])
        paraXor = []

        #Mostrado
        print(primerEstado, "      ",xor1,"         ", segundoEstado, "      ",xor2,"                   ", secuencia[i])


    print("\n\nRealimentación 1:  ", realimentacion1, "\n")
    print("Realimentación 2:  ", realimentacion2, "\n")
    print("Secuencia C/A:  ", secuencia, "\n")

principal("1111111111","1111111111")