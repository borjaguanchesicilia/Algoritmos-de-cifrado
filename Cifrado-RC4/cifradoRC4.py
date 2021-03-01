# Author: Borja Guanche Sicilia
# Mail: bg.sicilia@gmail.com
# Date: 23/02/2021
# File cifradoRC4.py: Implementación del cifrado RC4.

semilla = [2, 5]
texto = [1, 34]
S = []
K = []
for i in range(256):
    S.append(i)
    K.append(semilla[i % len(semilla)])

j = 0
for i in range(256):
    j = ((j + S[i] + K[i]) % 256)
    S[i], S[j] = S[j], S[i]

print(S)

secuaciaCifrante = []
k = i = j = 0
while(k < len(texto)):
    i = (i + 1) % 256
    j = (j+S[i]) % 256
    S[i], S[j] = S[j], S[i]
    t = (S[i]+S[j]) % 256
    secuaciaCifrante.append(t)
    k += 1

for i in range(len(secuaciaCifrante)):
    secuaciaCifrante[i] = S[secuaciaCifrante[i]]
    secuaciaCifrante[i] = str(bin(secuaciaCifrante[i])[2:]) 

print(secuaciaCifrante)


textoBinario = []
for i in range(len(texto)):
    textoBinario.append(str(bin(texto[i])[2:]))

print(textoBinario)


textoCifrado = []
for i in range(len(textoBinario)):
    textoCifrado.append(int(bin(int(textoBinario[i], 2) ^ int(secuaciaCifrante[i], 2))[2:]))
    #convertimos a int base 2


print(textoCifrado)