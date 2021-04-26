def exponenciacionRapida(a, b, m):

    x = 1
    y = a % m

    print("\n\ny:       b:       x:")
    print( y,"      ",b,"      ",x)

    while (b >0) and (y>1):
        
        if (b % 2 != 0):

            x = (x * y) % m
            b = b - 1
            print( "         ",round(b),"      ",x)
        else:

            y = (y * y) % m
            b = b / 2
            print( y,"      ",round(b))

    return (x)