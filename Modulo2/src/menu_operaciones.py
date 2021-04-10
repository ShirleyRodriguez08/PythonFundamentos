# 1. Importo las librerias
import math

# 2. Declarar constantes



# 3. Funciones

def sumar(a,b):
    return a + b

def resta(a, b):
    return a - b

def promedio_numeros(cantidad):
    numeros = []
    for n in range(cantidad):
        a = int(input(f'ingrese el {n+1} número: '))
        numeros.append(a)
        
    suma = 0
    for num in numeros:
        #print(num)
        suma += num

    return suma  / cantidad 


# 4. Mi programa

print("Bienvenido al menú interactivo")

while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Sumar dos numeros
    2) promedio de numeros
    3) Salir del programa""")
    opcion = input()

    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ", sumar(n1, n2))
        break
    elif opcion == '2':
        c = int(input('Ingrese la cantidad de números a solicitar: '))

        promedio = promedio_numeros(c)
        print(f'El promedio de los números introducidos es {promedio}')
        break
    elif opcion =='3':
        print("Adios")
        break
    else:
        print("Los datos ingresados son incorrectos")
