
def ingresa_numero_entero(mensaje=""):
    while True:
        try:
            n = int(input(mensaje))
            break
        except:
            print("Ha ocurrido un error, introduce bien el número")
    return n

def ingresa_numero(mensaje=""):
    while True:
        try:
            n = float(input(mensaje))
            break
        except:
            print("Ha ocurrido un error, introduce bien el número")
    return n
    

def ingresa_cadena(mensaje : str):
    return input(mensaje)


if __name__=='__main__':

    n1 = ingresa_numero('Ingrese un numeor flotante: ')
    print(n1)