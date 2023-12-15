posicion1 = 0
posicion2 = 7
for columnas in range(0,7):
    for filas in range(0,7):
        print('0')
    print()
print('   ',end='')
for letra in range(ord('a'),ord('i')):
    print(chr(letra), end='  ')