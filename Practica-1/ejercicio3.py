
import math
def promedio(numeros):
    total = 0
    for x in numeros:
        total += x
    return total / len(numeros)

def desviacion(numeros):
    prom = promedio(numeros)
    suma = 0
    for x in numeros:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (len(numeros) - 1))

valores = input("ingrese 10 números separados: ").split()
numeros = [float(x) for x in valores]
prom = promedio(numeros)
desv = desviacion(numeros)
print(f"el promedio es {prom:.2f}")
print(f"la desviación estandard es {desv:.5f}")
