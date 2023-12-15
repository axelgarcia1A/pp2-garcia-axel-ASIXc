"""
Nom: Axel Garcia Hernandez
ASIXc 1A M03 UF1
Data: 15/12/2023
Descripció:
Reemplaçar un caracter d'una frase per un altre demanat.
"""
palabra = input('Introdueix una frase? ')
sustituir = input('Quin caràcter vols remplaçar? ')
caracter = input('Que caracter quieres poner? ')

palabra_mod = ""

for x in palabra:
    if x == sustituir:
        palabra_mod += caracter
    else:
        palabra_mod += x

print('RESULTAT:',palabra_mod)