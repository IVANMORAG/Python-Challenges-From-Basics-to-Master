"""
EJERCICIO 42:
Solicita al usuario ingresar un número N y 
luego imprime la suma de todos 
desde 1 hasta N.
"""

num = int(input("Ingresa un número: "))

contador = 0

for i in range(1, num+1):
    contador = contador + 1
    suma = i + contador
    print(suma)