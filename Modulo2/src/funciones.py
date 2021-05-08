
def formula_triangulo(h, i):
    return " " * (h-i) + "#" * i


# 1. Pedir al usuario la cantidad de números a ingresar
h = int(input('Ingrese la altura del triangulo: '))

for i in range(1, h + 1 ):
    x = formula_triangulo(h,i)
    print(x)

