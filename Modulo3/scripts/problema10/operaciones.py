


def suma(a,b):
    try:
        return a + b
    except:
        print('Error: Tipo de dato no válido!')
    

def resta(a,b):
    try:
        return a - b
    except :
        print('Error: Tipo de dato no válido!')

def producto(a, b):
    try:
        return a * b
    except :
        print('Error: Tipo de dato no válido!')

def division(a , b):
    try:
        return a / b
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
    except TypeError:
        print('Error: Tipo de dato no válido!')


if __name__ == '__main__':

    x = 12
    y = 6
    z = 0
    w = "hola"
    
    # test 1
    print(f'la suma de {x} , {y} es : {suma(x,y)}')

    # test 2
    print(f'la resta de {x} , {w} es : {resta(x, w)}')
    
    # test 3
    print(f'la division de {x} , {y} es : {division(x, y)}')
    # test 4
    print(f'la division de {x} , {w} es : {division(x, w)}')

    # test 5
    print(f'la division de {x} , {z} es : {division(x, z)}')