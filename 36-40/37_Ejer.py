"""
EJERCICIO 37:
Calcula el máximo de 3 números.
"""


a, b, c = input("Ingrese tres números: ").split()

a , b, c = int(a, b, c)

if a > b and a > c:
    print(f"{a} es el mayor.")
elif b > a and b > c:
    print(f"{b} es el mayor")
else:
    print(f"{c} es el mayor.")