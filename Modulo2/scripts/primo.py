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

numero  =  int(input("Ingrese un numero: "))

if isPrimo(numero):
    print(f"el numero {numero} es primo")
else:
    print(f"el numero {numero} NO es primo")


