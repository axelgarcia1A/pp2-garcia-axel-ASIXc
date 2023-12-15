"""
Nom: Axel Garcia Hernandez
ASIXc 1A M03 UF1
Data: 15/12/2023
Descripció:
Calcular notes sense dewcimals d'11 alumnes i sapiguer si són suspesos o aprobats.
"""
nota= input().split(' ')
aprobat = []
suspes = []

for x in range(0,11):
    if nota == 5 or nota == 6 or nota == 7 or nota == 8 or nota == 9 or nota == 10:
        aprobat += nota
        print(aprobat)
    elif nota == 4 or nota == 3 or nota == 2 or nota == 1 or nota == 0:
        suspes += nota
        print(suspes)