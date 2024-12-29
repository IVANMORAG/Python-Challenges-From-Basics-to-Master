"""
EJERCICIO 40:
Calcular el IMC e 
interpretarlo.
"""

peso = input("Ingrese su peso en kg: ")
estatura = input("Ingrese su estatura en cm: ")

peso = float(peso)
estatura = float(peso)

imc = peso / (estatura * estatura)

print(imc)