import sys
import math

def mi_funcion():

    return NotImplementedError


def hola():
    print('Hola como estas?')

def saludar(nombre:str):

    print(f'Hola {nombre}, como estas ?')

def potenciacion(numero:float, potencia:int=2):
    """Devuelve la potencia de un numero elevado a la potencia

    Parameters
    ----------
    numero : float
        Description of parameter `numero`.
    potencia
        Description of parameter `potencia`

    Returns
    -------
    float
    Description of anonymous integer return value.
   """
    return math.pow(numero,potencia)

# ----------------------------------
# Mi programa principal
# ----------------------------------

# n = input('Ingresa tu nombre: ')
# saludar(n)

# print(mi_funcion())

numero = float(input('Ingrese un numero: '))

n = int(input('Ingrese un exponente: '))

x = potenciacion(numero, n)

potenciacion(15,3)



print(f'La potencia de {numero}, elevado a {n} es : {x}')

print(f'potencia de 2 es {potenciacion(2)}')
