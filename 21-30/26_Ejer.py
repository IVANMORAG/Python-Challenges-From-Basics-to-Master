"""
EJERCICIO 26:
Intercambia los valores  de dos variables
con asignación múltiple.
"""

a, b = input("Ingrese dos valores para A y B: ").split()

a = int(a)
b = int(b)

a, b =  b, a

print(f"a: {a}\n b: {b}")