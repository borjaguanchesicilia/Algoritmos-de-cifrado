from funciones import * 

def elGamalEliptico(p, a, b, G, da, db, m, ficheroEuclidesExten):

    puntosX = calculosPuntosX(p, a, b)
    puntosY = calculosPuntosY(p)

    puntosValidos = []

    for i in range(p):
        for j in range(p):
            if (puntosX[j][1] == puntosY[i][0]):
                puntosValidos.append([puntosX[j][0], puntosY[i][1]])

    puntosValidos = sorted(puntosValidos)
    print("Los puntos de la curva: ", puntosValidos)


    # Calculamos las claves públicas:

    clavePublicaBob = sumaPuntos(a, db, G, p, ficheroEuclidesExten)
    clavePublicaAlice = sumaPuntos(a, da, G, p, ficheroEuclidesExten)

    print(f'La clave pública de Bob: dbG --> {db}*({G[0]},{G[1]}) = ({clavePublicaBob[0]}, {clavePublicaBob[1]})')
    print(f'La clave pública de Alice: daG --> {da}*({G[0]},{G[1]}) = ({clavePublicaAlice[0]}, {clavePublicaAlice[1]})')


    # Calculamos las clave secreta compartida:

    claveSecretaCompartidaAlice = sumaPuntos(a, da, clavePublicaBob, p, ficheroEuclidesExten)
    claveSecretaCompartidaBob = sumaPuntos(a, db, clavePublicaAlice, p, ficheroEuclidesExten)

    print(f'La clave secreta compartida calculada por Alice: {da}*({clavePublicaBob[0]},{clavePublicaBob[1]}) = ({claveSecretaCompartidaAlice[0]},{claveSecretaCompartidaAlice[1]})')
    print(f'La clave secreta compartida calculada por Bob: {db}*({clavePublicaAlice[0]},{clavePublicaAlice[1]}) = ({claveSecretaCompartidaBob[0]},{claveSecretaCompartidaBob[1]})')


    # Codificamos el mensaje:

    mensajeCodificado = codificarMensaje(p, m, puntosValidos)


    # Ciframos el mensaje:

    mensajeCifrado = sumaPuntosDistintos(p, claveSecretaCompartidaAlice, mensajeCodificado, ficheroEuclidesExten)

    print("El mensaje cifrado y la clave pública enviados de A a B: {Qm + da * (dbG), daG} = ", "{", f'({mensajeCifrado[0]},{mensajeCifrado[1]}), ({clavePublicaAlice[0]},{clavePublicaAlice[1]})', "}")


    # Pintamos los puntos válidos

    graficarPuntos(puntosValidos, a, b)