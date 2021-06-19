def solicitar_entero(mensaje = 'Introduce un número entero: '):
    try:
        n = int(input(mensaje))
        return n
    except:
        print("Ha ocurrido un error, introduce bien el número")
        return solicitar_entero(mensaje)

def solicitar_float(mensaje = 'Introduce un número float: '):
    try:
        n = float(input(mensaje))
        return n
    except:
        print("Ha ocurrido un error, introduce bien el número")
        return solicitar_entero(mensaje)