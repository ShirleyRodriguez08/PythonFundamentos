# 1. librerias de programa

# 2. cosntantes


# 3. funciones y/o clases

def ingreso_entero(msg = 'Ingrese un numero : '):
    """
    Funcion que solicita el ingreso de un numero por teclado

    Parameters
    ----------
    msg : str
        Mensaje a ingresar `msg`.
    """
    try:
        return (int(input(msg)))
    except:
        print("Ha ocurrido un error, introduce bien el número")
        return ingreso_entero(msg)

# 4. mi programa
if __name__ == '__main__':
    # demo
    ingreso_entero()
    
    pass

