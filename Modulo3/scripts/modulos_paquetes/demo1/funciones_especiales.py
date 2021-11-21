import math

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