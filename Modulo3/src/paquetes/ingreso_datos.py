
def ingrese_numero(mensaje):
    try:
        num = int(input(mensaje))
        return num
    except:
        print('Vuelva a intentar')
        return ingrese_numero(mensaje)

def ingrese_numero_float(mensaje):
    try:
        num = float(input(mensaje))
        return num
    except:
        print('Vuelva a intentar')
        return ingrese_numero(mensaje)

# Porgrama
if __name__=="__main__":
    msg = "Ingrese un numero entero: "
    x = ingrese_numero(msg)
    print(x)