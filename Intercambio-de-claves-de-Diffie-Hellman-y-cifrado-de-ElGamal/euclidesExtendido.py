def euclidesExtendido(x, y):
   
    if x < y:
        return euclidesExtendido(y, x)

    a = x
    z = [0, 1]
    i = 0
    print("i        xi              zi")
    print(i, "      ",  "               ",z[0])
    i = i + 1
    print(i, "      ",x,  "             ",z[1])
    while y != 0:
        div = x // y
        x, y = y, x % y
        aux = ((div*(-1))*z[1]+z[0]) % a
        z.append(aux)
        z.pop(0)
        i = i + 1
        print(i, "      ",x,  "             ",z[1])

    return z[0]