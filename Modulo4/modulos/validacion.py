


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