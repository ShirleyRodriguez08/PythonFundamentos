# 1. Importar librerias
import os
import math

# 2. Definir constantes


# 3. FUnciones y/o metodos

# 4. Mi programa

a = input("Introducir el primer número: ")
b = int(input("Introducir el segundo número: "))

# derefiniendo mi variable como número
a = int(a)

c = a + b

# Salida del programa
# print(c)
print("La suma de los números es {}".format(c))

# print("La resta de los números a={} - b={} es: {}".format(a,b, a-b))

# otra forma de impresión
print(f"La resta de los números a={a} - b={b} es: {a-b}")

# 
print("La multiplicacion es: ", a * b)

# potencia 
p = math.pow(a,2)
print(f"el número a={a} elevado a la 2 es: {p}")
