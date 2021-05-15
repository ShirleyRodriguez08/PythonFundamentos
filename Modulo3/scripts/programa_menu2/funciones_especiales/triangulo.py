# 1. Importacion de librerias

# librerias python
import os

# 2. Constantes
DOLAR=3.68

# 3. Fuciones y/o Clases
def mostrar_triangulo(n):
    for i in range(n):
        x = i * 2 +1
        for e in range(x,0,-2):
            print(e,end=' ')
        print()

# 4. Mi programa

if __name__=='__main__':
    try:
        print('Ejecutando demo n=4')
        n = 4
        mostrar_triangulo(n)
    except Exception as e:
        print(e)

