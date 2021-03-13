


def val_num_float(text):
    """
    Permite validar el ingreso de un número

    Parameters
    ----------
    text : str
        Texto del input `text`.
    """
    while True :
        try:
            n = float(input(f"{text}: "))
            return n
        except:
            print("Ha ocurrido un error, introduce bien el número")


def val_num_int(text):
    """
    Permite validar el ingreso de un número

    Parameters
    ----------
    text : str
        Texto del input `text`.
    """
    while True :
        try:
            n = int(input(f"{text}: "))
            return n
        except:
            print("Ha ocurrido un error, introduce bien el número")


# prueba
# solo ejecuta esta parte si programa a ejecutar es 'valida.py'
if __name__ == "__main__":
    print(val_num_int('Ingrese un entero a manera de demo'))