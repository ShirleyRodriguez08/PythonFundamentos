# 1. Librerias
import math

# 2. Constantes


# 3.Funciones o/y clases

def ingrese_entero(msg : str = "Ingrese un numero: ") -> int :
    """Retorna un numero entero ingresado por teclado
    """
    try:
        n =  int(input(msg))
        return n
    except:
        print("Ingrese bien el numero")
        return ingrese_entero(msg)

def funcion_factorial(n: int ):
    """El factorial de un numero.

    Parameters
    ----------
    n : int
        Numero entero `n`.
    
    Returns
    -------
    int
        Retorna el factorial del numero `n`
   """

    facto= 1
    for i in range(1,n+1):
        facto = facto * i

    return facto

# 4. Mi programa

n = ingrese_entero()
factorial = funcion_factorial(n)
print(f"El factorial de {n} es {factorial}")


