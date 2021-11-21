# librerias python
import datetime

# librerias propias
from matematicas import operaciones 
from matematicas import funciones_especiales
from triangulos import triangulos as t

import clases
import utils


# Funciones y/o clases

def opcion1():
    a  =  utils.ingrese_float("Introduce un numero: ")
    b  =  utils.ingrese_float("Introduce un numero: ")
    resultado = operaciones.sumar(a, b)
    print(f"La suma de los numeros es {resultado}")

def opcion2():
    n  =  utils.ingrese_entero("Introduce un numero: ")
    factorial = funciones_especiales.funcion_factorial(n)
    print(f"El factorial es: {factorial}")


def opcion3():
    h  =  int(input("Introduce un numero: "))
    t.mostrar_triangulo(h)

def opcion4():
    nombre = input("Ingrese el nombre del restaurante: ")
    cusine = input("Ingrese el tipo de comida del restaurante: ")
    restaurante1 = clases.Restaurant(nombre, cusine)
    restaurante1.describe_restaurant()


def main():
    print("Bienvenido al menú interactivo")
    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        1) Sumar dos números
        2) Factorial de un números
        3) Mostrar triangulo
        4) Clase Restaurante
        5) Salir""")

        opcion = input()
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion =='3':
            opcion3()
        elif opcion =='4':
            opcion4()
        elif opcion =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")

# mi programa
if __name__ == "__main__":
    main()
    print("fin del codigo")