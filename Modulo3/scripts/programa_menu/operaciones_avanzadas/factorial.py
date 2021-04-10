# importar librerias
import math
import os
import sys

# 2. Constantes

# 3. Funciones 
def factorial_num( num :int):
    """
    Retorna el factorial de un número dado

    Parameters
    ----------
    num : int
    Numero a calcular su factorial `num`.

    Returns
    -------
    int
        Description of anonymous integer return value.

    """
    factorial = 1

    for n in range(2,num +1):
        factorial = factorial * n
    return factorial

# Inicia mi programa
if __name__ == "__main__":
    num = 10
    # Imprimo el factorial
    print('El factorial del numero {} es : {}'.format(num,factorial_num(num)))


