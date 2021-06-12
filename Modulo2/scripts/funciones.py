import math

def sumar_valores_lista(*args):
    suma_lista = 0
    for num in args:
        suma_lista += num
    return suma_lista

def potencia(x,y):
    return math.pow(x,y)

def saludar(nombre='Juan'):
    print(f'hola {nombre}')

def mostrar_triangulo(h):
    for i in range(1,h+1):
        print('#'*i)

def MostrarTriangulo():
    return NotImplemented

# mi programa
p = math.pow(2,4)
x = math.pow(12,2)

a = 3 ** 4

# potencia 3 * 4
b = potencia(3,4)

# print(b, a)
# saludar()

# mostrar_triangulo(6)

suma_valores = sumar_valores_lista(12,14,15,16,20,0,1)
print(f'la suma de los valores es: {suma_valores}')


