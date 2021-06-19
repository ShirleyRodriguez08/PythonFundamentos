
import validacion_datos as v

def mostrar_triangulo(altura):
    for i in range(1,altura+1):
        print('#'*i)


if __name__ == '__main__':
    altura = v.solicitar_entero('Ingrese la altura del triangulo programa "triangulo": ')
    mostrar_triangulo(altura)