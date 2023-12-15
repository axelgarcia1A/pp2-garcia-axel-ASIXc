"""
Nom: Axel Garcia Hernandez
ASIXc 1A M03 UF1
Data: 15/12/2023
Descripció:
    Fer un 8x8 de 0 i que la diagonal que va desde el 0,0 al 7,7 sigui 1
    i la que va de 0,7 al 7,0 sigui 2.
"""

posicion1 = 0
posicion2 = 7
for columnas in range(0,7):
    print(0*7,end=' ')
    for filas in range(0,7):
        print(0*7,end=' ')
        for x in range (posicion1,posicion2):
            print(1)
            posicion1 += 1
        for i in range (posicion2,posicion1):
            print(2)
            posicion2 -= 1
    print()

