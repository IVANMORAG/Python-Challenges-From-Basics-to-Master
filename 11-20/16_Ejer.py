""""
EJERCICIO 16:
Determina si una palabra es
palíndromo.
"""

palabra = input("Ingrese una palabra: ")

if palabra == palabra[::-1]:
    print(f"{palabra} es un palindromo.")
else:
    print(f"{palabra} no es un palindromo.")