"""
EJERCICIO 15:
Ordena una lista de números 
de menor a mayor.
"""

lista = list(map(int, input("Ingrese los números: ").split()))

lista.sort()

print(lista)