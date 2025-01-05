"""
EJERCICIO 7:
Dado un año. determina si es
bisiesto.
Regla:
    - Divisible por 4.
    - No divisible por 100.
    - Divisible por 400.
"""

anio = int(input("Ingrese el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")