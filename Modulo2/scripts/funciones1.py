# 1. Importar Librerias
import sys

# 2. Mis funciones y/o clases

def sumar(numero1, numero2):
    suma =  numero1 + numero2
    return suma # retornar un valor

# 3. Inicio de mi programa

a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))

# llamando a funcion
suma = sumar(a,b)

print('La suma de valores es {}'.format(suma))

