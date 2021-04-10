
def valida_numero(msg : str = 'Ingrese un numero: '):
    while True:
        try:
            x   =  int(input(msg))
            break
        except:
            print('ingrese bien el dato ... ')
    return x

def valida_float(msg : str = 'Ingrese un numero flotante: '):
    while True:
        try:
            x   =  float(input(msg))
            break
        except:
            print('ingrese bien el dato ... ')
    return x

# demo funcionamiento
# if name valida si el programa esta siendo importado
if __name__ == "__main__":
    print(valida_numero())