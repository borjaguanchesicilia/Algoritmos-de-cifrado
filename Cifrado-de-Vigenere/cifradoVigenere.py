abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

#texto = input("Introduzca el texto: ")
texto = "ESTE MENSAJE SE AUTODESTRUIRA"
texto = texto.replace(" ", "")
#clave = input("Introduzca la clave: ")
clave = "MISION"

textoNum = []
for i in range(len(texto)):
    for j in range(len(abc)):
        if (texto[i] == abc[j]):
            textoNum.append(j)

print(textoNum)


claveNum = []
tam = len(clave)
for i in range(tam):
    for j in range(len(abc)):
        if (clave[i] == abc[j]):
            claveNum.append(j)
    
print(claveNum)