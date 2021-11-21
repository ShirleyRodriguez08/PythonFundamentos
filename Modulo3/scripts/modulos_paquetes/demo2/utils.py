

def ingrese_entero(msg : str = "Ingrese un numero: ") -> int :
    """Retorna un numero entero ingresado por teclado
    """
    try:
        n =  int(input(msg))
        return n
    except:
        print("Ingrese bien el numero")
        return ingrese_entero(msg)

def ingrese_float(msg : str = "Ingrese un numero: ") -> float :
    """Retorna un numero float ingresado por teclado
    """
    try:
        n =  float(input(msg))
        return n
    except:
        print("Ingrese bien el numero")
        return ingrese_entero(msg)



