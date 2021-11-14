# 1. Importar Librerias
import math
import os
import sys 

# 2. Declarar constantes
PI = 3.14

# 3. Colocar funciones y/o clases

def isPrimo(numero):
    primo = True
    for i in range(2, numero):
        if numero % i ==0 :
            primo = False
            break
    return primo

# 4. Mi programa
listado_numeros  =  [*range(1,200)]

# para cada numero esvaluo si es primo o no es es
for numero in listado_numeros:
    # evaluo si es primo
    if isPrimo(numero):
        print(f"el numero {numero} es primo")


