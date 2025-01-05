"""
EJERCICIO 6:
Solicita el precio de un producto y calcula 
el precio final con un 16% de IVA
"""

precio = float(input("Ingrese el precio de su producto: "))

IVA = precio * 0.16
precioFinal = IVA + precio

print(f"Total a pagar: ${precioFinal}")