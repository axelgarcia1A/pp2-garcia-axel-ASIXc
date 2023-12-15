"""
Nom: Axel Garcia Hernandez
ASIXc 1A M03 UF1
Data: 15/12/2023
Descripció:
Reemplaçar un caracter d'una frase per un altre demanat.
"""

#Començament
palabra = input('Introdueix una frase? ')
sustituir = input('Quin caràcter vols remplaçar? ')
caracter = input('Que caracter quieres poner? ')


#Variable on es guardara tota la informació
palabra_mod = ""

#Bucle que comproba si el caracter está a la frase. El bucle converteix la frase en una llista
#i va comprobant-ho tot.

for x in palabra:
    if x == sustituir:
        palabra_mod += caracter
    else:
        palabra_mod += x

#Frase modificada
print('RESULTAT:',palabra_mod)