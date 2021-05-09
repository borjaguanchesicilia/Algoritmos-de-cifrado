from dhElgamalElipticos import * 

def main():

    p = 13
    a = 5
    b = 3
    G = [9, 6]
    da = 4
    db = 2
    m = 2

    elGamalEliptico(p, a, b, G, da, db, m)

main()