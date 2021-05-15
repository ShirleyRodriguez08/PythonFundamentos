import os


# valores a ser sumados se encuentran en una lista
def sumar(a,b):
    return a+b

def sumar_arg(*args):
    suma = 0
    for arg in args:
        suma += arg 
    return suma

# lista con valores a ser sumados
numeros_sumar=[23,11]

numeros_sumar2 = [23,11,1,2,3,4,5]

print(sumar(*numeros_sumar))

print(sumar_arg(*numeros_sumar2))