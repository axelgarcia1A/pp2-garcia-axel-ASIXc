"""
Nom: Axel Garcia Hernandez
ASIXc 1A M03 UF1
Data: 15/12/2023
Descripció:
Calcular notes sense dewcimals d'11 alumnes i sapiguer si són suspesos o aprobats.
"""

#Començament
notas = input().split(' ')
aprobado = []
suspendido = []

#Variables necessaries per fer tot.
ap = 0
sup = 0
no = 0
x = 0

#Bucle
try:
    for nota in notas:
        nota = int(nota)
        no +=1
        if no <= 11:
            if 5 <= nota <= 10:
                aprobado += [nota]
                ap += 1
            elif 0 <= nota <= 4:
                suspendido += [nota]
                sup += 1
        else:
            print('Demasiados alumnos')
except:
    print('Valor/es no valido')

#Resultat final
print(': ( Supesos:',sup)
print(suspendido)
print(': ) Aprovats:',ap)
print(aprobado)


