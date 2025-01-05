"""
EJERCICIO 3:
Calcula el promedio de tres números
dados por el usuario.
"""

a = list(map(int, input("Ingrese tres números: ").split()))

promedio = sum(a) / len(a)

print(f"El promedio es: {promedio}")